#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidget>
#include "ui_mainwindow.h"


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void viewStockDetails(QListWidgetItem * stock);
    void search();
    void updateDatabase();
    void switchToSingleView();
    void switchToListView();
    void switchToOneMonth();
    void switchToSixMonths();
    void switchToOneYear();
    void switchToAllTime();
    void updateGraph(float high,float low);
private:
    Ui::MainWindow *ui;
    void graph(QString timeframe);
    QString ticker;

};

#endif // MAINWINDOW_H
