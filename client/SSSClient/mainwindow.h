#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidget>
#include "ui_mainwindow.h"

QT_CHARTS_USE_NAMESPACE

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
    void updateGraph();
private:
    Ui::MainWindow *ui;

};

#endif // MAINWINDOW_H
