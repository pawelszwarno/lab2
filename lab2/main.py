import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random

def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    """Funkcja służąca do porównywania dwóch wykresów typu plot. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    label1(str): nazwa serii z pierwszego wykresu,
    label2(str): nazwa serii z drugiego wykresu.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 3 
    """
    if x1.shape != y1.shape or x2.shape != y2.shape or min(x1.shape)==0 or min(x2.shape)==0:
        return None
    fig, ax = plt.subplots()
    ax.plot(x1, y1,'b', linewidth=4, label=label1)
    ax.plot(x2, y2, 'r', linewidth=2, label=label2)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend()
    return fig

def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    """Funkcja służąca do stworzenia dwóch wykresów typu plot w konwencji subplot wertykalnie lub chorycontalnie. 
    Szczegółowy opis w zadaniu 5.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    x1label(str): opis osi x dla pierwszego wykresu,
    y1label(str): opis osi y dla pierwszego wykresu,
    x2label(str): opis osi x dla drugiego wykresu,
    y2label(str): opis osi y dla drugiego wykresu,
    title(str): tytuł wykresu,
    orientation(str): parametr przyjmujący wartość '-' jeżeli subplot ma posiadać dwa wiersze albo '|' jeżeli ma posiadać dwie kolumny.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 5
    """
    if x1.shape != y1.shape or x2.shape != y2.shape or min(x1.shape)==0 or min(x2.shape)==0:
        return None
    fig = plt.figure()
    if orientation == '-':
        plt.suptitle(title)
        plt.subplot(2,1,1)
        plt.plot(x1,y1)
        plt.xlabel(x1label)
        plt.ylabel(y1label)
        plt.subplot(2,1,2)
        plt.plot(x2,y2)
        plt.xlabel(x2label)
        plt.ylabel(y2label)
    elif orientation == '|':
        plt.suptitle(title)
        plt.subplot(1,2,1)
        plt.plot(x1,y1)
        plt.xlabel(x2label)
        plt.ylabel(y2label)
        plt.subplot(1,2,2)
        plt.plot(x2,y2)
        plt.xlabel(x2label)
        plt.ylabel(y2label)
    else:
        return None
    return fig

def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    """Funkcja służąca do tworzenia wykresów ze skalami logarytmicznymi. 
    Szczegółowy opis w zadaniu 7.
    
    Parameters:
    x(np.ndarray): wektor wartości osi x,
    y(np.ndarray): wektor wartości osi y,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    log_axis(str): wartość oznacza:
        - 'x' oznacza skale logarytmiczną na osi x,
        - 'y' oznacza skale logarytmiczną na osi y,
        - 'xy' oznacza skale logarytmiczną na obu osiach.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x,y) zgody z opisem z zadania 7 
    """
    if log_axis == 'x':
        plt.plot(x, y, xlabel= xlabel, ylabel= ylabel)
        plt.title(title)
        plt.semilogx()
    elif log_axis == 'y':
        plt.plot(x, y, xlabel= xlabel, ylabel= ylabel)
        plt.title(title)
        plt.semilogy()
    elif log_axis == 'xy':
        plt.plot(x, y, xlabel= xlabel, ylabel= ylabel)
        plt.title(title)
        plt.loglogx()
        
    else:
        return None