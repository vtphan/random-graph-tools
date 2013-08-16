import os, sys, getopt
import random

HOW_MANY = 20

def with_prob(p):
    r = random.random()
    if r <= p: return 1
    return 0
##
def gen_graph(filename, n, p=0.5, directed=False, min_w=0, max_w=0):
    random.seed()
    file = open(filename, 'w')
    if directed: file.write("digraph G {\n")
    else: file.write("graph G {\n")
    file.write("\tnode [shape=circle];\n")
    for i in range(n):
        for j in range(i+1,n):
            if with_prob(p):
                if directed:
                    if with_prob(0.5):
                        file.write("\t%d -> %d" % (i,j))
                    else:
                        file.write("\t%d -> %d" % (j,i))
                else:
                    file.write("\t%d -- %d" % (i,j))
                if min_w == max_w: file.write(";\n")
                else:
                    w = random.randrange(min_w, max_w+1)
                    file.write(" [label=\"%d\"];\n" % (w))
    file.write("}\n");
    file.close()
    if directed: command = 'dot'
    else: command = 'neato'
    ex = command + ' -Tpng ' + filename + ' -o ' + filename+'.png'
    os.system( ex )
    print "output to files: ", filename," and", filename+'.png'
    print ex
    preview_ex = '/Applications/Preview.app/Contents/MacOS/Preview'
#    os.system( preview_ex + ' ' + filename+'.png' )


################################################
def usage():
    print "Purpose: generate random graphs"
    print "Usage python random-graphs -h"
    print "Usage python random-graphs [-d] n p [min_weight max_weight]"
    print "\tn\tnumber of vertices\n\tp\tedge probability\n\td\tdirected\n"
    sys.exit(0)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd")
    except getopt.GetoptError:
        usage()

    if not args or len(args)<2 or not args[0].isdigit() or int(args[0]) < 1 or float(args[1])<0 or float(args[1])>1: usage()
    directed = False
    for opt, arg in opts:
        if opt == '-h': usage()
        if opt == '-d': directed = True

    min_weight=max_weight=0
    if len(args)==4:
        min_weight = int(args[2])
        max_weight = int(args[3])
        if min_weight > max_weight: usage()

    for i in range(HOW_MANY):
        filename = 'output/_rand_granh.gv'
        gen_graph(filename+repr(i), int(args[0]), float(args[1]), directed, min_weight, max_weight)


if __name__ == "__main__":
    main(sys.argv[1:])

