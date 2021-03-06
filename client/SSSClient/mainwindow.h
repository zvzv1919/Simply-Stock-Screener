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
    void clearGraph();
    void updateGraphPoint(double time, double price, QLineSeries* ss);
    void updateDatabaseButton(int code, QProcess::ExitStatus status);
    void updateHistoricalData(int code, QProcess::ExitStatus status);
    void updateRealtimeData();
private:
    Ui::MainWindow *ui;
    void graph(QString timeframe);
    QString ticker;
    QProcess * updateprocess;
    QProcess * historicalprocess;
    QProcess * realtimeprocess;
};

#endif // MAINWINDOW_H
