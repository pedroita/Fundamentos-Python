# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:20:51 2020

@author: Pedro Italo
"""

def main ():
    n = int(input("Digite um numero inteiro não negativo"))
    i=1
    n_fat=1
    while i<=n:
        n_fat=n_fat*i
        i=i+1
    print("%d!= %d"%(n,n_fat))
main()