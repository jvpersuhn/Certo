import sys
sys.path.append("C:/Users/900143/Desktop/Certo")
from controller.squad_controller import BackController, FrontController,SGBDController , SquadController, BackEnd, FrontEnd, SGBD, Squad 
from flask import Flask, render_template, request, redirect

sqc = SquadController()
squad = sqc.select_byId(3)

print(squad)