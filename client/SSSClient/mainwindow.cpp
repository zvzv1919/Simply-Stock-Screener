#include "mainwindow.h"
#include "ui_mainwindow.h"

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
    ui->currentdatatable1->setItem(4,0, new QTableWidgetItem("52-week High:"));
    ui->currentdatatable1->setItem(5,0, new QTableWidgetItem("Market Cap:"));
    ui->currentdatatable1->setItem(6,0, new QTableWidgetItem("P/E Ratio:"));

    ui->currentdatatable2->setItem(2,0, new QTableWidgetItem("Previous Close:"));
    ui->currentdatatable2->setItem(3,0, new QTableWidgetItem("Day Low:"));
    ui->currentdatatable2->setItem(4,0, new QTableWidgetItem("52-week Low:"));
    ui->currentdatatable2->setItem(5,0, new QTableWidgetItem("Dividend Yield:"));

    ui->resultslist->addItem("NYSE:UTX");
    ui->resultslist->addItem("NYSE:SNAP");

    ui->currentdatatable1->setItem(0,1, new QTableWidgetItem("999.99"));
    ui->currentdatatable2->setItem(0,1, new QTableWidgetItem("+999.99 (100%)"));

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::viewStockDetails(QListWidgetItem * stock) {
    QString stockstring = stock->text();

    // TODO: Fork thread to perform search

    // Prepare data screen
    ui->stockname->setText(stockstring);
    for(int i = 0; i < ui->currentdatatable1->rowCount(); i++) {
        ui->currentdatatable1->setItem(i,1, nullptr);
    }
    for(int i = 0; i < ui->currentdatatable2->rowCount(); i++) {
        ui->currentdatatable2->setItem(i,1, nullptr);
    }

    // TODO: await thread return and fill table with data

    ui->pageswitcher->setCurrentWidget(ui->singleview);
}

void MainWindow::search() {
    QString query = ui->searchbar->text();
    ui->searchbar->clear();

    // TODO: Fork thread to perform search

    // Prepare searching screen
    ui->searchresults->setText("Searching...");
    ui->resultslist->clear();

    // TODO: await thread return and fill table with data
    ui->searchresults->setText("Search Results for: " + query);


    ui->pageswitcher->setCurrentWidget(ui->listview);
}

void MainWindow::updateDatabase() {
    // TODO: Fork thread to submit update database request
}

void MainWindow::switchToSingleView() {
    ui->pageswitcher->setCurrentWidget(ui->singleview);
}

void MainWindow::switchToListView() {
    ui->pageswitcher->setCurrentWidget(ui->listview);
}
