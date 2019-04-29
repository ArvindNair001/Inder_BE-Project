import argparse
# import test
import rntn as rntn
import tree as tr
# import rntn
from nltk import Tree
from nltk.treeprettyprinter import TreePrettyPrinter
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import os


DATA_DIR = "trees"


def tester(data,timestr):
    print('Executing main')
    print("Testing...")
    model = rntn.RNTN.load('models/RNTN.pickle')
    test_trees = tr.load_trees('test')
    cost, result = model.test(test_trees)
    accuracy = 100.0 * result.trace() / result.sum()
    print("Cost = {:.2f}, Correct = {:.0f} / {:.0f}, Accuracy = {:.2f} %".format(
            cost, result.trace(), result.sum(), accuracy))
    for tree in tr.parse(data):
        # return model.predict(tree).pretty_print()    
        # model.predict(tree)._repr_png_()

        cf = CanvasFrame()
        t = model.predict(tree)
        tc = TreeWidget(cf.canvas(),t)
        cf.add_widget(tc,10,10) # (10,10) offsets
        cf.print_to_file('tree.ps')
        cf.destroy()
        os.system('convert tree.ps ./static/images/tree-'+timestr+'.jpg')
        os.path
        
if __name__ == "__main__":
    tester()    
    



