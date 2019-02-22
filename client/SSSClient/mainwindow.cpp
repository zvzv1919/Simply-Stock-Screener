#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QProcess>
#include <QtDebug>
#include <QFileInfo>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Set up initial data table
    ui->currentdatatable1->setItem(0,0, new QTableWidgetItem("Current Price:"));
    ui->currentdatatable2->setItem(0,0, new QTableWidgetItem("Change:"));

    ui->currentdatatable1->setItem(2,0, new QTableWidgetItem("Day Open:"));
    ui->currentdatatable1->setItem(3,0, new QTableWidgetItem("Day High:"));
    ui->currentdatatable1->setItem(4,0, new QTableWidgetItem("Volume:"));

    ui->currentdatatable2->setItem(2,0, new QTableWidgetItem("Previous Close:"));
    ui->currentdatatable2->setItem(3,0, new QTableWidgetItem("Day Low:"));

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::viewStockDetails(QListWidgetItem * stock) {
    QString stockstring = stock->text();

    // Create process to retrieve data
    QProcess p;
    QString path = QFileInfo(".").absolutePath();
    QStringList params;
    path += "/../backend.py";
    params << path << "single" << stockstring;
    p.start("python.exe", params);

    // Prepare data screen
    ui->stockname->setText("");
    for(int i = 0; i < ui->currentdatatable1->rowCount(); i++) {
        ui->currentdatatable1->setItem(i,1, nullptr);
    }
    for(int i = 0; i < ui->currentdatatable2->rowCount(); i++) {
        ui->currentdatatable2->setItem(i,1, nullptr);
    }

    // Await process return and fill table with data -
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

    ui->pageswitcher->setCurrentWidget(ui->singleview);
}

void MainWindow::search() {
    QString query = ui->searchbar->text();
    ui->searchbar->clear();

    // Check if search is for single stock or list
    if(query.isUpper()) {
        QListWidgetItem stock(query);   // Deleted upon return from this function - Be careful with asynchronization
        viewStockDetails(&stock);
        return;
    }

    // Create thread to perform search
    QProcess p;
    QString path = QFileInfo(".").absolutePath();
    QStringList params;
    path += "/../backend.py";
    params << path << "search" << query;
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

    if(poutput.compare("\r\n") == 0) {
        ui->searchresults->setText("Search Results for: " + query + " : No results found");
        ui->pageswitcher->setCurrentWidget(ui->listview);
        return;
    }

    ui->searchresults->setText("Search Results for: " + query);

    // TODO: Display results in list

    ui->pageswitcher->setCurrentWidget(ui->listview);
}

void MainWindow::updateDatabase() {
    // TODO: Fork thread to submit update database request
}

void MainWindow::switchToOneMonth() {

}

void MainWindow::switchToSixMonths() {

}

void MainWindow::switchToOneYear() {

}

void MainWindow::switchToAllTime() {

}

void MainWindow::switchToSingleView() {
    ui->pageswitcher->setCurrentWidget(ui->singleview);
}

void MainWindow::switchToListView() {
    ui->pageswitcher->setCurrentWidget(ui->listview);
}
