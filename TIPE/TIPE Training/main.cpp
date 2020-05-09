#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <cmath>
#include <iostream>
#include <cereal/archives/binary.hpp>
#include <cereal/types/vector.hpp>
#include <cereal/types/tuple.hpp>
#include <SDL.h>
#include <thread>
using namespace std;

template<typename T>
string convertNbToStr(const T& number)
{
    ostringstream convert;
    convert << number;
    return convert.str();
}

void echo(string str)
{
    unsigned int time = SDL_GetTicks();
    string finalStr = convertNbToStr((time - (time % 1000)) / 1000) + "s " + str + "\n";
    cout << finalStr;
}

vector<tuple<vector<double>, unsigned short>> TRAINING;
vector<unsigned short> OLD_TRAINING;
unsigned int NB_ELEMENTS, THETA_NUMBER, TMP_WORKING_ELEMENTS, SIZE;
vector<vector<double>> oldTheta, theta, newTheta, H_THETA, E_MY_SUM;
vector<vector<unsigned short>> NEW_TRAINING;
double STEP;
unsigned short threads = 0;

double mySum(unsigned int picIndex, unsigned int numberIndex)
{
    double partialSum = 0;
    for(unsigned int j = 0; j < THETA_NUMBER; j++)
        partialSum += theta[numberIndex][j] * (get<0>(TRAINING[picIndex]))[j];
    return partialSum;
}

double h_theta(unsigned int picIndex, unsigned int numberIndex)
{
    double partialSum = theta[numberIndex][0];
    for(unsigned int i = 1; i < THETA_NUMBER; i++)
        partialSum += theta[numberIndex][i] * (get<0>(TRAINING[picIndex]))[i];
    return partialSum;
}

double dh_theta(unsigned int picIndex, unsigned int thetaIndex, unsigned int numberIndex)
{
    return (get<0>(TRAINING[picIndex]))[thetaIndex] / (1 + E_MY_SUM[numberIndex][picIndex]);
}

unsigned short prediction(unsigned int index, bool debug = false)
{
    unsigned int bestIndex = 0;
    double bestDistance = 10;
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        double hTet = h_theta(index, numberIndex);
        /*if(debug)
        {
            echo(convertNbToStr(hTet) + " " + convertNbToStr(bestDistance) + " " + convertNbToStr(numberIndex) + " " + convertNbToStr(bestIndex));
        }*/
        if(hTet < bestDistance)
        {
            bestIndex = numberIndex;
            bestDistance = hTet;
        }
    }
    return bestIndex;
}

void predictionRate()
{
    unsigned int nb = 0;
    for(unsigned int i = 0; i < NB_ELEMENTS; i++)
        if(OLD_TRAINING[i] == prediction(i))
            nb++;
    echo(convertNbToStr(100 * nb / NB_ELEMENTS) + " " + convertNbToStr(nb) + " " + convertNbToStr(NB_ELEMENTS));
}

unsigned short predictionIndex(unsigned int index)
{
    unsigned short prediction = 0;
    unsigned int nbIndex = 0;
    for(unsigned int i = 0; i < NB_ELEMENTS; i++)
        if(OLD_TRAINING[i] == index)
        {
            nbIndex++;
            if(!round(h_theta(i, index)))
                prediction++;
        }
    return prediction;
}

bool condition(unsigned short numberIndex)
{
    return true;
}

void digit(unsigned short numberIndex)
{
    if(condition(numberIndex))
        echo(convertNbToStr(numberIndex));
    unsigned short iteration = 0, predi = predictionIndex(numberIndex), lastImprove = 0;
    unsigned int lastValue = NB_ELEMENTS;
    while(predi <= lastValue)
    {
        if(predi == lastValue) lastImprove++;
        else lastImprove = 0;
        if(lastImprove == 2) break;
        lastValue = predi;
        if(condition(numberIndex))
            echo(convertNbToStr(numberIndex) + " ita " + convertNbToStr(iteration) + " " + convertNbToStr(predi));
        for(unsigned int k = 0; k < NB_ELEMENTS; k++)
        {
            H_THETA[numberIndex][k] = h_theta(k, numberIndex);
            E_MY_SUM[numberIndex][k] = exp(-mySum(k, numberIndex));
        }
        for(unsigned int i = 0; i < THETA_NUMBER; i++)
        {
            double sum = 0;
            for(unsigned int k = 0; k < NB_ELEMENTS; k++)
                sum += dh_theta(k, i, numberIndex) * (H_THETA[numberIndex][k] - NEW_TRAINING[numberIndex][k]);
            newTheta[numberIndex][i] = theta[numberIndex][i] - STEP * sum;
        }
        for(unsigned int i = 0; i < THETA_NUMBER; i++)
        {
            oldTheta[numberIndex][i] = theta[numberIndex][i];
            theta[numberIndex][i] = newTheta[numberIndex][i];
        }
        iteration++;
        predi = predictionIndex(numberIndex);
    }
    if(condition(numberIndex))
        echo(convertNbToStr(numberIndex) + " itb " + convertNbToStr(iteration) + " " + convertNbToStr(predi));
    for(unsigned int i = 0; i < THETA_NUMBER; i++)
        theta[numberIndex][i] = oldTheta[numberIndex][i];
    if(condition(numberIndex))
        echo(convertNbToStr(numberIndex) + " itc " + convertNbToStr(iteration) + " " + convertNbToStr(predi));
    threads--;
}

int main(int argc, char *argv[])
{
    ifstream file("train.bin", ifstream::binary);
    cereal::BinaryInputArchive iarchive(file);
    iarchive(TRAINING);
    iarchive(OLD_TRAINING);
    NB_ELEMENTS = OLD_TRAINING.size();
    file.close();

    //TMP_WORKING_ELEMENTS = 60000;
    THETA_NUMBER = (get<0>(TRAINING[0])).size();
    SIZE = (unsigned int)(sqrt(THETA_NUMBER));
    STEP = 0.02 / NB_ELEMENTS;

    vector<double> tmp0;
    for(unsigned int thetaIndex = 0; thetaIndex < THETA_NUMBER; thetaIndex++)
        tmp0.push_back(0);
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        oldTheta.push_back(tmp0);
        theta.push_back(tmp0);
        newTheta.push_back(tmp0);
    }
    tmp0.clear();
    for(unsigned int elementIndex = 0; elementIndex < NB_ELEMENTS; elementIndex++)
        tmp0.push_back(0);
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        H_THETA.push_back(tmp0);
        E_MY_SUM.push_back(tmp0);
        vector<unsigned short> tmp1;
        for(unsigned int pic = 0; pic < NB_ELEMENTS; pic++)
        {
            unsigned short isTheDigit = int(OLD_TRAINING[pic] != numberIndex);
            //echo(convertNbToStr(isTheDigit) + " " + convertNbToStr(OLD_TRAINING[pic]) + " " + convertNbToStr(numberIndex));
            tmp1.push_back(isTheDigit);
        }
        NEW_TRAINING.push_back(tmp1);
    }

    threads = 10;
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        thread digitThread(digit, numberIndex);
        //digitThread.join();
        digitThread.detach();
    }
    while(threads != 0)
    {
        SDL_Delay(100);
    }
    predictionRate();
    ofstream thetasFile("thetas.bin", fstream::binary);
    cereal::BinaryOutputArchive oarchive(thetasFile);
    oarchive(theta);
    thetasFile.close();
    thetasFile.open("thetas.txt");
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        for(unsigned int thetaIndex = 0; thetaIndex < THETA_NUMBER; thetaIndex++)
        {
            thetasFile << theta[numberIndex][thetaIndex] << " ";
        }
        thetasFile << "\n";
    }
    thetasFile.close();

    //prediction(0, true);
}

/*

216575s 1
0s 5
0s 0
0s 2
0s 3
0s 7
0s 6
0s 8
0s 4
0s 9
0s 3 ita 0 6131
0s 0 ita 0 5923
0s 4 ita 0 5842
0s 8 ita 0 5851
0s 2 ita 0 5958
0s 6 ita 0 5918
0s 7 ita 0 6265
0s 9 ita 0 5949
0s 5 ita 0 5421
0s 1 ita 0 6742
5s 8 ita 1 5429
5s 2 ita 1 5814
5s 0 ita 1 5665
5s 5 ita 1 5313
5s 4 ita 1 5811
5s 3 ita 1 5979
5s 1 ita 1 6739
7s 6 ita 1 5819
8s 7 ita 1 6243
8s 9 ita 1 5878
11s 4 ita 2 3116
11s 2 ita 2 2125
11s 3 ita 2 2313
11s 8 ita 2 1220
11s 0 ita 2 1906
13s 5 ita 2 2483
14s 1 ita 2 6208
16s 6 ita 2 2482
16s 7 ita 2 3988
16s 8 ita 3 286
16s 2 ita 3 723
16s 9 ita 2 2481
16s 4 ita 3 1289
16s 3 ita 3 940
19s 0 ita 3 798
22s 5 ita 3 1084
22s 4 ita 4 762
22s 3 ita 4 539
22s 8 ita 4 122
22s 7 ita 3 1983
22s 1 ita 3 4979
22s 9 ita 3 829
22s 6 ita 3 935
25s 2 ita 4 416
27s 0 ita 4 575
28s 6 ita 4 563
28s 8 ita 5 92
28s 4 ita 5 607
28s 1 ita 4 4214
28s 9 ita 4 469
28s 5 ita 4 701
29s 3 ita 5 450
29s 7 ita 4 1341
33s 2 ita 5 323
33s 4 ita 6 585
33s 0 ita 5 555
33s 5 ita 5 570
33s 6 ita 5 482
33s 9 ita 5 367
33s 1 ita 5 3939
35s 8 ita 6 76
37s 3 ita 6 436
37s 7 ita 5 1157
39s 5 ita 6 519
39s 4 itb 7 602
39s 4 itc 7 602
39s 9 ita 6 337
39s 6 ita 6 475
39s 2 ita 6 306
41s 0 itb 6 612
41s 0 itc 6 612
41s 1 ita 6 3899
44s 8 ita 7 71
44s 2 itb 7 307
44s 2 itc 7 307
44s 7 ita 6 1139
44s 9 ita 7 331
44s 3 itb 7 454
44s 6 itb 7 508
44s 3 itc 7 454
44s 6 itc 7 508
44s 5 ita 7 503
49s 1 itb 7 3965
49s 1 itc 7 3965
50s 8 itb 8 74
50s 8 itc 8 74
50s 9 itb 8 341
50s 5 itb 8 504
50s 9 itc 8 341
50s 5 itc 8 504
50s 7 itb 7 1181
50s 7 itc 7 1181
58s 73 44206 60000

Process returned 60000 (0xEA60)   execution time : 59.761 s
Press any key to continue.

*/
