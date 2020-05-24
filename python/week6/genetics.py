def populationGraph(recessive, dominant, mixed):
    import pylab
    numOrganisms = recessive[0] + dominant[0] + mixed[0]
    pylab.plot(range(len(recessive)), recessive, label="tt")
    pylab.plot(range(len(dominant)), dominant, label="TT")
    pylab.plot(range(len(mixed)), mixed, label="Tt and tT")
    pylab.legend(loc='upper left')
    pylab.axis([0,len(recessive),0,numOrganisms])
    pylab.xlabel('Number of Generations')
    pylab.ylabel('Number of Organisms')
    pylab.show()
