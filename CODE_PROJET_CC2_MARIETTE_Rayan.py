# =============================================================================
# Nom du fichier : CODE_PROKET_CC2_Rayan.py
# Auteur : MARIETTE Rayan
# Année : 2021-2022
# Classe : ITS2
# Sujet : Methode Simplexe ' Linear Programming'
# Professeur : Thiago ABREU
# Lien Github : https://github.com/greunder/CC2
# =============================================================================


def Pas_Simple():
    
    s=0.05
    x1=0.0
    f1=0.0
    def x(xi):
        if xi>0:
            return x1+(xi-1)*s
        else:
            return x1+(xi+1)*s
    
    
    def main_function(xi):
        return  x(xi)**5-5*x(xi)**3-20*x(xi)+5
    
    def Recherche_pas_fixe():
        xi=1
        if main_function(2)<main_function(1) :
            while main_function(xi+1)<main_function(xi): 
                xi=xi+1
            valeur=x(xi-1)
            valeur_1=x(xi)
        elif main_function(2)>main_function(1):
            while main_function(xi+1)>main_function(xi):
                xi=xi-1
            valeur=x(xi-1)
            valeur_1=x(xi)
        elif main_function(2)==main_function(3):
           valeur=x(1)
           valeur_1=x(2)
        elif main_function(2)>main_function(1) :
            valeur=x(-2)
            valeur_1=x(2)
        return xi,valeur,valeur_1
    
    results=Recherche_pas_fixe()
    xi=results[0]
    valeur=results[1]
    valeur_1=results[2]
    print("L'optimum se situe entre ",valeur," et ",valeur_1,". f(x')=",main_function(xi))

def PA():
    def Pas_Acc(xi,s,x1):
        
        if xi>0:
            return x1+(xi-1)*s
        else:
            return x1+(xi+1)*s
    
    
    def main_Function(xi,s,x1):
            return Pas_Acc(xi,s,x1)**5-5*Pas_Acc(xi,s,x1)**3-20*Pas_Acc(xi,s,x1)+5
        
    def pas_acc():
            x1=0.0
            s=0.05
            xi=1
            if main_Function(2,s,x1)<main_Function(1,s,x1) :
                while main_Function(xi+1,s,x1)<main_Function(xi,s,x1): 
                    xi+=1
                    s=2*s
                a=Pas_Acc(xi-1,s,x1)
                b=Pas_Acc(xi,s,x1)
            if main_Function(2,s,x1)>main_Function(1,s,x1):
                while main_Function(xi+1,s,x1)>main_Function(xi,s,x1):
                    xi-=1
                    s=2*s
                a=Pas_Acc(xi-1,s,x1)
                b=Pas_Acc(xi,s,x1)
            elif main_Function(2,s,x1)==main_Function(3,s,x1):
                a=Pas_Acc(1,s,x1)
                b=Pas_Acc(2,s,x1)
            elif main_Function(2,s,x1)>main_Function(1,s,x1) and main_Function(2,s,x1)>main_Function(1,s,x1):
                a=Pas_Acc(-2,s,x1)
                b=Pas_Acc(2,s,x1)
            return xi,a,b,s
    results=pas_acc()
    xi=results[0]
    valeur=results[1]
    valeur_1=results[2]   
    s=results[3]
    print("\nL'optimum se situe entre :",valeur," et ",valeur_1)
        
    
    
    
def NR():
    def main_function(Function, x, tol = 0.0001, maxiter = 1000):
        for i in range (maxiter):
          xnew = x - Function[0](x)/Function[1](x)
          if abs(xnew - x) < tol: break
          x = xnew
        return xnew, i
    
    y = [lambda x: x**3 - 7*x**2 + 8*x-3, lambda x: 3*x**2 - 14*x+8]
    x,n = main_function(y,5)
    
    print("\nL'optimum est atteint à %f à l'itération n° %d" %(x,n))
    
    
    
NR()    
Pas_Simple()
PA()
