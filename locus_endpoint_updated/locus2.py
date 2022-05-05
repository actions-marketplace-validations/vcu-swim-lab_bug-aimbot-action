import subprocess
import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import shutil


def runLocus():
    #os.system('java -jar locusrunnable.jar configfile.txt')
    os.system('java -jar locusEveryLang.jar configfile.txt')
    #x = subprocess.check_output('java -jar locusrunnable.jar configfile.txt', shell=True)
    x = subprocess.check_output('java -jar locusEveryLang.jar configfile.txt', shell=True)
    print(x)


def createConfig(repoFolder):
    f = open("configfile.txt", "w+")

    task = "all"
    f.write('task='+task + "\n")
    f.write('repoDir=' + repoFolder + "\n")
    f.write('sourceDir=' + repoFolder + "\n")
    workingLoc = "/home/saprad_vcu/locus_endpoint/work"
    isdir1 = os.path.isdir(workingLoc)
    print(isdir1)
    if isdir1:
        shutil.rmtree(workingLoc)    
        subprocess.call('mkdir ' + workingLoc, shell=True)
    
    f.write('workingLoc='+  workingLoc + "\n")
    bugReport = '/home/saprad_vcu/locus_endpoint/output.xml'
    f.write('bugReport='+bugReport + "\n")
    f.close()


def make_bugreport(name,id,oDate,summarytxt, descriptiontxt):   #need to add files to fixed files
    root = Element('bugrepository')
    root.set('name', name)
    bug = Element('bug')
    bug.set('id', id)
    #bug.set('opendate', "2010-03-30 04:03:07")
    bug.set('opendate', oDate)
    #bug.set('fixdate', "2010-04-01 03:04:39")
    bug.set('fixdate', oDate)
    root.append(bug)
    buginfo = Element('buginformation')
    bug.append(buginfo)
    summary = etree.SubElement(buginfo, 'summary')
    summary.text = summarytxt
    description = etree.SubElement(buginfo, 'description')
    description.text = descriptiontxt
    fixedfiles = Element('fixedFiles')
    bug.append(fixedfiles)
    tree = ElementTree(root)
    with open('output.xml', 'wb') as file:
        tree.write(file)


def cloneRepo(url):
    repo = '/home/saprad_vcu/locus_endpoint/repo'
    isdir = os.path.isdir(repo)
    print(isdir)
    if isdir:
        shutil.rmtree(repo)

    subprocess.call('git clone --depth 5000 ' + url + ' /home/saprad_vcu/locus_endpoint/repo', shell=True)
    print('cloning the repository')
    return repo


def readOutput():
    ranking = open('/home/saprad_vcu/locus_endpoint/work/ranking_Locus.tsv', "r")
    return ranking.read()




