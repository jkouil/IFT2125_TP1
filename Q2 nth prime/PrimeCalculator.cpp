//Nom, Matricule
//Nom, Matricule

#include "PrimeCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>


// ce fichier contient les definitions des methodes de la classe PrimeCalculator
// this file contains the definitions of the methods of the PrimeCalculator class

PrimeCalculator::PrimeCalculator()
{
}

using namespace std;
vector<bool> numbers;

int PrimeCalculator::CalculateNthPrime(int N)
{
    if (N > 0)
    {
        int tmp = N;
        //Le théorème de Rosser (source.Wikipedia)
        N = round(N * log(N) + N * log(log(N)));

        //on sait que le theoreme du Rosser fonctionne pour tout n > 6 (source.Wikipedia)
        if (N < 6) N = 6;

        // Vecteur des nombres de 2 à n
        //On créé une liste des nombres de 2 à n
        vector<bool> numbers(N + 1, true);
        numbers[0] = false;
        numbers[1] = false;

        // Crible d'Eratosthene (source.Wikipedia)
        // On peux se limiter à d ≤ √n (car c’est impossible d’avoir uniquement des facteurs qui sont > √n)
        // Le +1 sur la borne supérieure du range est importante pour exclure les carrés parfaits 4, 9, 16, …
        for (int i = 2; i <= floor(sqrt(N)); i++) {

            //si number[i] == True (donc potentiellement premier)
            if (numbers[i]) {
                //On itère j de 2*i à n(soit les multiples des numbers[i])
                // Et on met à False dans numbers tous les multiples de i.
                // Cela permet de rayer les multiples de i, qui sont donc non premier
                for (int j = 2 * i; j <= N; j += i)
                    numbers[j] = false;
            }
        }

        // vecteur qui Récupére les nombres premiers
        vector<int> primes;
        //On itère i de 2 jusqu'à n(tout le tableau).
        //si number[i] == True alors il est premier
        for (int i = 2; i <= N; i++) {

            if (numbers[i])
                primes.push_back(i);
        }

        int result = primes[tmp - 1];
        return result;

    }else{

        return 0;
    }
}
