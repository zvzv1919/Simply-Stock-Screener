/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSingleview;
    QAction *actionListview;
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QGroupBox *displaygroupbox;
    QGridLayout *gridLayout_2;
    QStackedWidget *pageswitcher;
    QWidget *singleview;
    QGridLayout *gridLayout_4;
    QScrollArea *singleviewscrollarea;
    QWidget *scrollAreaWidgetContents_2;
    QVBoxLayout *verticalLayout_2;
    QTextEdit *stockname;
    QGroupBox *currentdatatablebox;
    QHBoxLayout *horizontalLayout;
    QTableWidget *currentdatatable1;
    QTableWidget *currentdatatable2;
    QWidget *listview;
    QVBoxLayout *verticalLayout_3;
    QTextEdit *searchresults;
    QListWidget *resultslist;
    QGroupBox *searchbargroupbox;
    QGridLayout *gridLayout_3;
    QLineEdit *searchbar;
    QTextEdit *textEdit;
    QGroupBox *sidebargroupbox;
    QVBoxLayout *verticalLayout;
    QTextEdit *textEdit_2;
    QPushButton *updatebutton;
    QSpacerItem *verticalSpacer;
    QMenuBar *menuBar;
    QMenu *menuDebug;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1274, 669);
        actionSingleview = new QAction(MainWindow);
        actionSingleview->setObjectName(QString::fromUtf8("actionSingleview"));
        actionListview = new QAction(MainWindow);
        actionListview->setObjectName(QString::fromUtf8("actionListview"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        displaygroupbox = new QGroupBox(centralWidget);
        displaygroupbox->setObjectName(QString::fromUtf8("displaygroupbox"));
        displaygroupbox->setBaseSize(QSize(0, 0));
        gridLayout_2 = new QGridLayout(displaygroupbox);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        pageswitcher = new QStackedWidget(displaygroupbox);
        pageswitcher->setObjectName(QString::fromUtf8("pageswitcher"));
        singleview = new QWidget();
        singleview->setObjectName(QString::fromUtf8("singleview"));
        gridLayout_4 = new QGridLayout(singleview);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        singleviewscrollarea = new QScrollArea(singleview);
        singleviewscrollarea->setObjectName(QString::fromUtf8("singleviewscrollarea"));
        singleviewscrollarea->setStyleSheet(QString::fromUtf8("border: transparent;"));
        singleviewscrollarea->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 1017, 473));
        scrollAreaWidgetContents_2->setAutoFillBackground(false);
        scrollAreaWidgetContents_2->setStyleSheet(QString::fromUtf8(""));
        verticalLayout_2 = new QVBoxLayout(scrollAreaWidgetContents_2);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        stockname = new QTextEdit(scrollAreaWidgetContents_2);
        stockname->setObjectName(QString::fromUtf8("stockname"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(stockname->sizePolicy().hasHeightForWidth());
        stockname->setSizePolicy(sizePolicy);
        stockname->setMinimumSize(QSize(0, 50));
        stockname->setMaximumSize(QSize(16777215, 50));
        QFont font;
        font.setPointSize(24);
        stockname->setFont(font);
        stockname->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));
        stockname->setReadOnly(true);

        verticalLayout_2->addWidget(stockname);

        currentdatatablebox = new QGroupBox(scrollAreaWidgetContents_2);
        currentdatatablebox->setObjectName(QString::fromUtf8("currentdatatablebox"));
        horizontalLayout = new QHBoxLayout(currentdatatablebox);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        currentdatatable1 = new QTableWidget(currentdatatablebox);
        if (currentdatatable1->columnCount() < 2)
            currentdatatable1->setColumnCount(2);
        if (currentdatatable1->rowCount() < 7)
            currentdatatable1->setRowCount(7);
        currentdatatable1->setObjectName(QString::fromUtf8("currentdatatable1"));
        currentdatatable1->setFocusPolicy(Qt::NoFocus);
        currentdatatable1->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));
        currentdatatable1->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        currentdatatable1->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        currentdatatable1->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        currentdatatable1->setAutoScroll(false);
        currentdatatable1->setEditTriggers(QAbstractItemView::NoEditTriggers);
        currentdatatable1->setTabKeyNavigation(false);
        currentdatatable1->setProperty("showDropIndicator", QVariant(false));
        currentdatatable1->setDragDropOverwriteMode(false);
        currentdatatable1->setSelectionMode(QAbstractItemView::NoSelection);
        currentdatatable1->setSelectionBehavior(QAbstractItemView::SelectItems);
        currentdatatable1->setTextElideMode(Qt::ElideRight);
        currentdatatable1->setShowGrid(false);
        currentdatatable1->setGridStyle(Qt::NoPen);
        currentdatatable1->setCornerButtonEnabled(false);
        currentdatatable1->setRowCount(7);
        currentdatatable1->setColumnCount(2);
        currentdatatable1->horizontalHeader()->setVisible(false);
        currentdatatable1->horizontalHeader()->setHighlightSections(false);
        currentdatatable1->horizontalHeader()->setStretchLastSection(false);
        currentdatatable1->verticalHeader()->setVisible(false);
        currentdatatable1->verticalHeader()->setHighlightSections(false);

        horizontalLayout->addWidget(currentdatatable1);

        currentdatatable2 = new QTableWidget(currentdatatablebox);
        if (currentdatatable2->columnCount() < 2)
            currentdatatable2->setColumnCount(2);
        if (currentdatatable2->rowCount() < 6)
            currentdatatable2->setRowCount(6);
        currentdatatable2->setObjectName(QString::fromUtf8("currentdatatable2"));
        currentdatatable2->setFocusPolicy(Qt::NoFocus);
        currentdatatable2->setLayoutDirection(Qt::LeftToRight);
        currentdatatable2->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));
        currentdatatable2->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        currentdatatable2->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        currentdatatable2->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        currentdatatable2->setAutoScroll(false);
        currentdatatable2->setEditTriggers(QAbstractItemView::NoEditTriggers);
        currentdatatable2->setTabKeyNavigation(false);
        currentdatatable2->setProperty("showDropIndicator", QVariant(false));
        currentdatatable2->setDragDropOverwriteMode(false);
        currentdatatable2->setSelectionMode(QAbstractItemView::NoSelection);
        currentdatatable2->setSelectionBehavior(QAbstractItemView::SelectItems);
        currentdatatable2->setTextElideMode(Qt::ElideRight);
        currentdatatable2->setShowGrid(false);
        currentdatatable2->setGridStyle(Qt::NoPen);
        currentdatatable2->setCornerButtonEnabled(false);
        currentdatatable2->setRowCount(6);
        currentdatatable2->setColumnCount(2);
        currentdatatable2->horizontalHeader()->setVisible(false);
        currentdatatable2->horizontalHeader()->setHighlightSections(false);
        currentdatatable2->horizontalHeader()->setStretchLastSection(false);
        currentdatatable2->verticalHeader()->setVisible(false);
        currentdatatable2->verticalHeader()->setCascadingSectionResizes(false);
        currentdatatable2->verticalHeader()->setHighlightSections(false);

        horizontalLayout->addWidget(currentdatatable2);

        horizontalLayout->setStretch(0, 1);
        horizontalLayout->setStretch(1, 1);

        verticalLayout_2->addWidget(currentdatatablebox);

        singleviewscrollarea->setWidget(scrollAreaWidgetContents_2);

        gridLayout_4->addWidget(singleviewscrollarea, 0, 0, 1, 1);

        pageswitcher->addWidget(singleview);
        listview = new QWidget();
        listview->setObjectName(QString::fromUtf8("listview"));
        verticalLayout_3 = new QVBoxLayout(listview);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        searchresults = new QTextEdit(listview);
        searchresults->setObjectName(QString::fromUtf8("searchresults"));
        sizePolicy.setHeightForWidth(searchresults->sizePolicy().hasHeightForWidth());
        searchresults->setSizePolicy(sizePolicy);
        searchresults->setMinimumSize(QSize(0, 50));
        searchresults->setMaximumSize(QSize(16777215, 50));
        QFont font1;
        font1.setPointSize(12);
        searchresults->setFont(font1);
        searchresults->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));
        searchresults->setReadOnly(true);

        verticalLayout_3->addWidget(searchresults);

        resultslist = new QListWidget(listview);
        resultslist->setObjectName(QString::fromUtf8("resultslist"));
        resultslist->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));
        resultslist->setEditTriggers(QAbstractItemView::NoEditTriggers);
        resultslist->setProperty("showDropIndicator", QVariant(false));
        resultslist->setItemAlignment(Qt::AlignLeading);

        verticalLayout_3->addWidget(resultslist);

        pageswitcher->addWidget(listview);

        gridLayout_2->addWidget(pageswitcher, 0, 0, 1, 1);


        gridLayout->addWidget(displaygroupbox, 2, 2, 1, 1);

        searchbargroupbox = new QGroupBox(centralWidget);
        searchbargroupbox->setObjectName(QString::fromUtf8("searchbargroupbox"));
        searchbargroupbox->setBaseSize(QSize(0, 0));
        gridLayout_3 = new QGridLayout(searchbargroupbox);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        searchbar = new QLineEdit(searchbargroupbox);
        searchbar->setObjectName(QString::fromUtf8("searchbar"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(searchbar->sizePolicy().hasHeightForWidth());
        searchbar->setSizePolicy(sizePolicy1);
        searchbar->setMaximumSize(QSize(16777215, 45));

        gridLayout_3->addWidget(searchbar, 1, 0, 1, 2);

        textEdit = new QTextEdit(searchbargroupbox);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        sizePolicy1.setHeightForWidth(textEdit->sizePolicy().hasHeightForWidth());
        textEdit->setSizePolicy(sizePolicy1);
        textEdit->setMinimumSize(QSize(400, 10));
        textEdit->setMaximumSize(QSize(450, 45));
        textEdit->setSizeIncrement(QSize(0, 0));
        textEdit->setBaseSize(QSize(0, 0));
        textEdit->setAutoFillBackground(false);
        textEdit->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));
        textEdit->setReadOnly(true);

        gridLayout_3->addWidget(textEdit, 0, 0, 1, 1);

        gridLayout_3->setRowStretch(0, 1);
        gridLayout_3->setColumnStretch(0, 2);

        gridLayout->addWidget(searchbargroupbox, 1, 2, 1, 1);

        sidebargroupbox = new QGroupBox(centralWidget);
        sidebargroupbox->setObjectName(QString::fromUtf8("sidebargroupbox"));
        sidebargroupbox->setBaseSize(QSize(0, 0));
        verticalLayout = new QVBoxLayout(sidebargroupbox);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        textEdit_2 = new QTextEdit(sidebargroupbox);
        textEdit_2->setObjectName(QString::fromUtf8("textEdit_2"));
        textEdit_2->setMinimumSize(QSize(150, 100));
        textEdit_2->setStyleSheet(QString::fromUtf8(" background-color: rgba(0, 0, 0, 0);border: transparent;"));

        verticalLayout->addWidget(textEdit_2);

        updatebutton = new QPushButton(sidebargroupbox);
        updatebutton->setObjectName(QString::fromUtf8("updatebutton"));

        verticalLayout->addWidget(updatebutton);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        verticalLayout->setStretch(0, 2);
        verticalLayout->setStretch(1, 1);
        verticalLayout->setStretch(2, 9);

        gridLayout->addWidget(sidebargroupbox, 1, 0, 2, 2);

        gridLayout->setRowStretch(1, 1);
        gridLayout->setRowStretch(2, 5);
        gridLayout->setColumnStretch(1, 1);
        gridLayout->setColumnStretch(2, 5);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1274, 21));
        menuDebug = new QMenu(menuBar);
        menuDebug->setObjectName(QString::fromUtf8("menuDebug"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuDebug->menuAction());
        menuDebug->addAction(actionSingleview);
        menuDebug->addAction(actionListview);

        retranslateUi(MainWindow);
        QObject::connect(actionSingleview, SIGNAL(triggered()), MainWindow, SLOT(switchToSingleView()));
        QObject::connect(actionListview, SIGNAL(triggered()), MainWindow, SLOT(switchToListView()));
        QObject::connect(resultslist, SIGNAL(itemClicked(QListWidgetItem*)), MainWindow, SLOT(viewStockDetails(QListWidgetItem*)));
        QObject::connect(searchbar, SIGNAL(returnPressed()), MainWindow, SLOT(search()));
        QObject::connect(updatebutton, SIGNAL(clicked()), MainWindow, SLOT(updateDatabase()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSingleview->setText(QApplication::translate("MainWindow", "Singleview", nullptr));
        actionListview->setText(QApplication::translate("MainWindow", "Listview", nullptr));
        displaygroupbox->setTitle(QString());
        stockname->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>", nullptr));
        stockname->setPlaceholderText(QApplication::translate("MainWindow", "Stockname Goes Here", nullptr));
        currentdatatablebox->setTitle(QString());
        searchresults->setPlaceholderText(QApplication::translate("MainWindow", "Search Results for:", nullptr));
        searchbargroupbox->setTitle(QString());
        textEdit->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Search for a single stock, or specify criterea to search for</span></p></body></html>", nullptr));
        sidebargroupbox->setTitle(QString());
        textEdit_2->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Welcome to Simply Stock Screener!</span></p></body></html>", nullptr));
        updatebutton->setText(QApplication::translate("MainWindow", "Update Database", nullptr));
        menuDebug->setTitle(QApplication::translate("MainWindow", "Debug", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
