#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidget>

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
    void switchToSingleView();
    void switchToListView();

private:
    Ui::MainWindow *ui;

};

#endif // MAINWINDOW_H
