#include "mainwindow.h"

#include <QProcess>
#include <QtDebug>
#include <QFileInfo>
#include <QtCharts>

QT_CHARTS_USE_NAMESPACE


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ticker = "";

    // Set up initial data table
    ui->currentdatatable1->setItem(0,0, new QTableWidgetItem("Current Price:"));
    ui->currentdatatable2->setItem(0,0, new QTableWidgetItem("Change:"));

    ui->currentdatatable1->setItem(2,0, new QTableWidgetItem("Day Open:"));
    ui->currentdatatable1->setItem(3,0, new QTableWidgetItem("Day High:"));
    ui->currentdatatable1->setItem(4,0, new QTableWidgetItem("Volume:"));

    ui->currentdatatable2->setItem(2,0, new QTableWidgetItem("Previous Close:"));
    ui->currentdatatable2->setItem(3,0, new QTableWidgetItem("Day Low:"));

    QStringList headerlist;
    headerlist << "Date" << "Price";
    ui->historicaldatatable->setHorizontalHeaderLabels(headerlist);

    QLineSeries *defaultSeries = new QLineSeries();
    QChart *chart = new QChart();

    defaultSeries->append(0,0);
    chart->addSeries(defaultSeries);
    chart->createDefaultAxes();

    QValueAxis *axisX =new QValueAxis;
        axisX->setRange(0,12);
        axisX->setGridLineVisible(true);
        axisX->setTickCount(11);
        axisX->setMinorTickCount(5);

     QValueAxis *axisY=new QValueAxis;
            axisY->setRange(-10,10);
            axisY->setGridLineVisible(true);
            axisY->setTickCount(6);
            axisY->setMinorTickCount(2);

     chart->setAxisX(axisX,defaultSeries);
     chart->setAxisY(axisY,defaultSeries);
     chart->legend()->hide();
     chart->createDefaultAxes();

     chart->setTitle("Stock Price");
     ui->currentQcharts->setChart(chart);
     ui->currentQcharts->setRenderHint(QPainter::Antialiasing);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::viewStockDetails(QListWidgetItem * stock) {
    QString stockstring = stock->text();
    ticker = stockstring;

    // Create process to retrieve current data
    QProcess p;
    QString path = QFileInfo(".").absolutePath();
    QStringList params;
    path += "/../backend.py";
    params << path << "single" << stockstring;
    p.start("python.exe", params);

    // Create process to retrieve historical data
    QProcess p2;
    QStringList params2;
    params2 << path << "historical" << stockstring;
    p2.start("python.exe", params2);



    // Prepare data screen
    ui->stockname->setText("");
    for(int i = 0; i < ui->currentdatatable1->rowCount(); i++) {
        ui->currentdatatable1->setItem(i,1, nullptr);
    }
    for(int i = 0; i < ui->currentdatatable2->rowCount(); i++) {
        ui->currentdatatable2->setItem(i,1, nullptr);
    }

    ui->historicaldatatable->clearContents();
    ui->historicaldatatable->setRowCount(0);
    ui->historicaldatatable->setMinimumHeight(0);

    // Await current data process return and fill table with data -
    if(!p.waitForFinished(-1)) {
        qDebug() << "Error with process";
        ui->stockname->setText(stockstring.append(" - Error receiving data"));
        ui->pageswitcher->setCurrentWidget(ui->singleview);
        return;
    }
    QString poutput(p.readAllStandardOutput());

    qDebug() << poutput;

    if(poutput.compare("\r\n[\'{}\']\r\n") == 0) {
        ui->stockname->setText(stockstring.append(" - Stock not found"));
        ui->pageswitcher->setCurrentWidget(ui->singleview);
        return;
    }
    int ind = poutput.indexOf('[');
    ind = poutput.indexOf('[', ind+1);
    poutput = poutput.mid(ind+1, poutput.length() - ind - 1 - 3);
    poutput = poutput.remove('\'');
    QStringList datalist = poutput.split(", ");
    ui->currentdatatable1->setItem(0,1, new QTableWidgetItem(datalist[4]));

    ui->currentdatatable2->setItem(0,1, new QTableWidgetItem(datalist[8] + " (" + datalist[9] + ")"));

    ui->currentdatatable1->setItem(2,1, new QTableWidgetItem(datalist[1]));
    ui->currentdatatable1->setItem(3,1, new QTableWidgetItem(datalist[2]));
    ui->currentdatatable1->setItem(4,1, new QTableWidgetItem(datalist[5]));

    ui->currentdatatable2->setItem(2,1, new QTableWidgetItem(datalist[7]));
    ui->currentdatatable2->setItem(3,1, new QTableWidgetItem(datalist[3]));

    ui->stockname->setText(stockstring + " - " + datalist[6]);

    // Wait for historical process to be finished
    if(!p2.waitForFinished(-1)) {
        qDebug() << "Error with process";
        ui->pageswitcher->setCurrentWidget(ui->singleview);
        return;
    }

    QString histline = p2.readLine();
    while(!histline.isEmpty()) {
        QStringList histlist = histline.left(histline.size() - 4).split(' ');
        int rowcnt = ui->historicaldatatable->rowCount();
        ui->historicaldatatable->insertRow(rowcnt);
        ui->historicaldatatable->setItem(rowcnt,0, new QTableWidgetItem(histlist[0]));
        ui->historicaldatatable->setItem(rowcnt,1, new QTableWidgetItem(histlist[1]));
        histline = p2.readLine();
    }

    // Resize historical data table to contents
    if(ui->historicaldatatable->rowCount() > 0) {
        int height = ui->historicaldatatable->horizontalHeader()->height() + ui->historicaldatatable->rowCount() * ui->historicaldatatable->verticalHeader()->sectionSize(0);
        ui->historicaldatatable->setMinimumHeight(height);
    }

    // TODO: Write lines to table

    // Switch to single view
    ui->pageswitcher->setCurrentWidget(ui->singleview);
}

void MainWindow::search() {
    QString query = ui->searchbar->text();
    QString sdate = ui->startdate->text();
    QString edate = ui->enddate->text();
    ui->searchbar->clear();
    ui->startdate->clear();
    ui->enddate->clear();
    // Check if search is for single stock or list
    if(query.isUpper()) {
        QListWidgetItem stock(query); // Deleted upon return from this function - Be careful with asynchronization
        viewStockDetails(&stock);
        return;
    }

    // Create thread to perform search
    QProcess p;
    QString path = QFileInfo(".").absolutePath();
    QStringList params;
    path += "/../backend.py";
    params << path << "search" << query;

    // Check if time limit needed
    if(sdate.isEmpty()) {
        sdate = "sot";
    }
    if(edate.isEmpty()) {
        edate = "present";
    }
    params << sdate;
    params << edate;

    // Start process
    p.start("python.exe", params);

    // Prepare searching screen
    ui->searchresults->setText("Searching...");
    ui->resultslist->clear();

    // Await process return and fill list with data
    if(!p.waitForFinished(-1)) {
        qDebug() << "Error with process";
        ui->searchresults->setText("Search Results for: " + query + " : Error with process");
        ui->pageswitcher->setCurrentWidget(ui->listview);
        return;
    }
    QString poutput(p.readAllStandardOutput());
    qDebug() << poutput;

    // Format sdate so it is human-readable
    if(sdate.compare("sot") == 0) {
        sdate = "start of time";
    }

    if(poutput.compare("") == 0) {
        ui->searchresults->setText("Search Results for: " + query + " from " + sdate + " to " + edate + " : No results found");
        ui->pageswitcher->setCurrentWidget(ui->listview);
        return;
    }

    ui->searchresults->setText("Search Results for: " + query + " from " + sdate + " to " + edate);

    // Display results in list
    QStringList searchlist = poutput.split("\r\n");
    for(int i = 0; i < searchlist.length(); i++) {
        ui->resultslist->addItem(searchlist[i]);
    }


    ui->pageswitcher->setCurrentWidget(ui->listview);
}

void MainWindow::updateDatabase() {
    // Disable updatebutton during update
    ui->updatebutton->setEnabled(false);
    ui->updatebutton->setText("Updating Database...");

    // Create process to update database
    updateprocess = new QProcess(this);
    QString path = QFileInfo(".").absolutePath();
    QStringList params;
    path += "/../backend.py";
    params << path << "update";

    // Connect process finished signal to updatebutton slot
    connect(updateprocess, SIGNAL(finished(int,QProcess::ExitStatus)), this, SLOT(updateDatabaseButton(int, QProcess::ExitStatus)));

    updateprocess->start("python.exe", params);
}

void MainWindow::graph(QString timeframe) {

    // Create process to retrieve data

    //QProcess p;
    QString path = QFileInfo(".").absolutePath();
    QStringList params;
    path += "/../backend.py";
    /*params << path << "graph" << ticker << timeframe;
    p.start("python.exe", params);
    */
    clearGraph();
    // TODO: clear graph
    // Await process return and fill list with data
    /*if(!p.waitForFinished(-1)) {
        qDebug() << "Error with process";
        return;
    }
    QString poutput(p.readAllStandardOutput());
    qDebug() << poutput;
    */

    QLineSeries *sp = new QLineSeries();
    QChart *newchart = new QChart();


    QProcess p3;
    QStringList params3;
    params3 << path << "historical" << ticker;
    p3.start("python.exe", params3);

    //Check the process thread
    if(!p3.waitForFinished(-1)) {
        qDebug() << "Error with process";
        return;
    }

    QString graphline = p3.readLine();

    QDateTime xValue;

    while(!graphline.isEmpty()) {
        QStringList graphlist = graphline.left(graphline.size() - 4).split(' ');

        //seperate year, date and month
        QStringList datelist = graphlist[0].split('-');
        xValue.setDate(QDate(datelist[0].toInt(),datelist[1].toInt(),datelist[2].toInt()));
        qreal yValue = graphlist[1].toDouble();
        sp->append(xValue.toMSecsSinceEpoch(), yValue);

        graphline = p3.readLine();
    }

    newchart->addSeries(sp);

    QDateTimeAxis *axisX = new QDateTimeAxis;
    axisX->setFormat("MM-dd-yyyy");
    newchart->addAxis(axisX, Qt::AlignBottom);
    sp->attachAxis(axisX);

    QValueAxis *axisY = new QValueAxis;
    newchart->addAxis(axisY, Qt::AlignLeft);
    sp->attachAxis(axisY);
    //TODO: Once get data,use a for loop to call UpdateGraphPoint() to plot sp
    newchart->setTitle("Stock Price");
    //newchart->createDefaultAxes();
    ui->currentQcharts->setChart(newchart);

}

void MainWindow::switchToOneMonth() {
    graph("1 month");
}

void MainWindow::switchToSixMonths() {
    graph("6 month");
}

void MainWindow::switchToOneYear() {
    graph("1 year");
}

void MainWindow::switchToAllTime() {
    graph("all");
}

void MainWindow::switchToSingleView() {
    ui->pageswitcher->setCurrentWidget(ui->singleview);
}

void MainWindow::switchToListView() {
    ui->pageswitcher->setCurrentWidget(ui->listview);
}

void MainWindow::clearGraph(){
    QLineSeries *series = new QLineSeries();
    QChart *chart = new QChart();
    QValueAxis *uaxisX =new QValueAxis;
        uaxisX->setRange(0,12);
        uaxisX->setGridLineVisible(true);
        uaxisX->setTickCount(11);
        uaxisX->setMinorTickCount(5);

     QValueAxis *uaxisY=new QValueAxis;
        uaxisY->setRange(-10,10);
        uaxisY->setGridLineVisible(true);
        uaxisY->setTickCount(6);
        uaxisY->setMinorTickCount(2);
        chart->setAxisX(uaxisX,series);
        chart->setAxisY(uaxisY,series);
        chart->legend()->hide();
        chart->createDefaultAxes();

            QFont *graphTitle= new QFont();
            graphTitle->setItalic(true);
            chart->setTitleFont(*graphTitle);
            chart->setTitle("Stock Price");
            ui->currentQcharts->setChart(chart);
}

void MainWindow::updateGraphPoint(double time, double price, QLineSeries* ss){
    ss->append(time,price);
}

void MainWindow::updateDatabaseButton(int code, QProcess::ExitStatus status) {
    if(code == 0) {
        ui->updatebutton->setText("Update Database");
        ui->updatebutton->setEnabled(true);
    }
    else {
        ui->updatebutton->setText("Database Update Failed");
    }
    delete updateprocess;
}
