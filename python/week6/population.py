"""
simulate population genetics

J. Knerr
May 2020
"""

# TT,Tt,tT are tall
# tt are short

import random
import genetics

def main():
    size = 100000
    prob = 0.5
    numgen = 200

    pop = initPop(size, prob)
    countGenotypes(pop,True)
    pop = manyGenerations(pop,numgen)
    countGenotypes(pop,True)

def manyGenerations(pop, num):
    """simulate num generations, return final population"""
    rec = []
    dom = []
    mix = []
    for i in range(num):
        pop = oneGeneration(pop)
        r,d,m = countGenotypes(pop,False)
        rec.append(r)
        dom.append(d)
        mix.append(m)
    genetics.populationGraph(rec,dom,mix)
    return pop

def oneGeneration(pop):
    """simulatate one generation, return new pop"""
    newpop = []
    for i in range(len(pop)):
        parent1 = random.choice(pop)
        parent2 = random.choice(pop)
        allele1 = random.choice(parent1)
        allele2 = random.choice(parent2)
        newpop.append(allele1+allele2)
    return newpop

def countGenotypes(pop,shouldprint):
    """print results for population"""
    dom = 0   # dominant  TT
    mix = 0   # mixed     Tt or tT
    rec = 0   # recessive tt
    for org in pop:
        if org == "TT":
            dom += 1
        elif org == "tt":
            rec += 1
        else:
            mix += 1
    d = dom/len(pop)
    m = mix/len(pop)
    r = rec/len(pop)
    if shouldprint:
        print("TT: %5.3f  Tt and tT: %5.3f  tt: %5.3f" % (d,m,r))
    return r,d,m

def initPop(popSize, p):
    """initialize population as list of strings"""
    # p = probability of having T vs t
    orgs = []
    for i in range(popSize):
        allele = ""
        for j in range(2):
            if random.random() < p:
                allele += "T"
            else:
                allele += "t"
        orgs.append(allele)
    return orgs

main()
