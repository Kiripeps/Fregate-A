import Skript1Dowload as sc1
import Skript2ChekBroken as sc2

#pathSha = input("Введите путь к папке для сохранения контрольной суммы: ")
#pathFile = input("Введите путь к папке для сохранения файлов: ")
pathSha = "E:\FilesSha"
pathFile = "E:\Files"

sc1.ftpDownload('FbaSha', pathSha)
sc1.ftpDownload('Fba', pathFile)

sc2.chekSum(pathFile, pathSha)
