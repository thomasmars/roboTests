import sys, time

start = time.time()
if __name__ == '__main__':
    print 'hello'
    gettingInput = True
    maxLoops = 500
    loops = 0

    while gettingInput and loops < maxLoops:
        line = sys.stdin.readline().strip()
        loops += 1

        if line == 'loop':
            print "elapsed time", str(time.time() - start)
            print "got lines", str(line)
            print "loops", str(loops)
            print "keep looping"
            pass
        elif line == '':
            pass
        else:
            print "elapsed time", str(time.time() - start)
            print "equals loop ?", line.strip() == 'loop'
            print "got lines", str(line)
            print "expected, got"
            print str(line)
            print "loop"
            print "loops", str(loops)
            print "stopping loop"
            gettingInput = False
