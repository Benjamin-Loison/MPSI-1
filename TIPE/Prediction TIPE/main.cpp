#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <cmath>
#include <iostream>
#include <cereal/archives/binary.hpp>
#include <cereal/types/vector.hpp>
#include <SDL.h>
#include <SDL_ttf.h>
#define SIZE 28
#define FACTOR 10
unsigned short FACTORxSIZE = SIZE * FACTOR;
using namespace std;

bool draw[SIZE][SIZE];
unsigned int THETA_NUMBER = SIZE * SIZE;
vector<vector<double>> theta;
vector<double> TESTING;
SDL_Color black = {0, 0, 255};
TTF_Font* font;
SDL_Renderer* renderer;
SDL_Texture* message;
double initialsDistances[10];

template<typename T>
string convertNbToStr(const T& number)
{
    ostringstream convert;
    convert << number;
    return convert.str();
}

void echo(string str)
{
    cout << str << endl;
}

double h_theta(unsigned int numberIndex)
{
    double partialSum = theta[numberIndex][0];
    for(unsigned int i = 1; i < THETA_NUMBER; i++)
        partialSum += theta[numberIndex][i] * TESTING[i];
    return partialSum;
}

unsigned short digit(double d)
{
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        if(initialsDistances[numberIndex] == d) return numberIndex;
    }
    return 10; // couldn't happened
}

unsigned short prediction()
{
    double distances[10], temp;
    for(unsigned short numberIndex = 0; numberIndex < 10; numberIndex++)
    {
        //echo(convertNbToStr(numberIndex) + " " + convertNbToStr(hTet) + " " + convertNbToStr(bestDistance));
        distances[numberIndex] = h_theta(numberIndex);
        initialsDistances[numberIndex] = distances[numberIndex];
    }

    for(unsigned short i = 0; i < 10; i++)
    {
        for(unsigned short j = i + 1; j < 10; j++)
        {
            // if there is a smaller element found on right of the array then swap it
            if(distances[j] < distances[i])
            {
                temp = distances[i];
                distances[i] = distances[j];
                distances[j] = temp;
            }
        }
    }

    message = SDL_CreateTextureFromSurface(renderer, TTF_RenderText_Solid(font, (convertNbToStr(digit(distances[0])) + convertNbToStr(digit(distances[1])) + convertNbToStr(digit(distances[2]))).c_str(), black));
}

void drawPxl(unsigned short x, unsigned short y)
{
    unsigned short realX = (x - x % FACTOR) / FACTOR, realY = (y - y % FACTOR) / FACTOR;
    draw[realY][realX] = true;
    //echo(convertNbToStr(realX) + " " + convertNbToStr(realY));
    TESTING[realY * SIZE + realX] = 1;
}

void clearTesting()
{
    TESTING.clear();
    for(unsigned short pxlIndex = 0; pxlIndex < THETA_NUMBER; pxlIndex++)
        TESTING.push_back(0);
    for(unsigned short y = 0; y < SIZE; y++)
        for(unsigned short x = 0; x < SIZE; x++)
            draw[y][x] = false;
    message = SDL_CreateTextureFromSurface(renderer, TTF_RenderText_Solid(font, "", black));
}

int main(int argc, char *argv[])
{
    SDL_Rect messageRect;
    messageRect.x = FACTORxSIZE;
    messageRect.y = 0;
    messageRect.w = 100;
    messageRect.h = 100;

    clearTesting();

    THETA_NUMBER = SIZE * SIZE;
    ifstream thetasFile("thetas.bin", ifstream::binary);
    cereal::BinaryInputArchive iarchive(thetasFile);
    iarchive(theta);
    thetasFile.close();

    bool quit = false, drawing = false;

    SDL_Event event;
    SDL_Init(SDL_INIT_VIDEO);
    TTF_Init();
    font = TTF_OpenFont("C:\\Windows\\Fonts\\arial.ttf", 200);
    SDL_Window* window = SDL_CreateWindow("TIPE Essai", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, FACTORxSIZE + 100, FACTORxSIZE + 1, 0);
    renderer = SDL_CreateRenderer(window, -1, 0);

    while(!quit)
    {
        SDL_WaitEvent(&event);

        switch (event.type)
        {
            case SDL_QUIT:
                quit = true;
                break;
            case SDL_MOUSEBUTTONDOWN:
                switch(event.button.button)
                {
                    case SDL_BUTTON_LEFT:
                        drawPxl(event.motion.x, event.motion.y);
                        prediction();
                        drawing = true;
                        break;
                }
                break;
            case SDL_MOUSEBUTTONUP:
                switch(event.button.button)
                {
                    case SDL_BUTTON_LEFT:
                        drawing = false;
                        break;
                }
                break;
            case SDL_MOUSEMOTION:
                if(drawing)
                {
                    drawPxl(event.motion.x, event.motion.y);
                    prediction();
                }
                break;
            case SDL_KEYDOWN:
                switch(event.key.keysym.sym)
                {
                    case SDLK_SPACE:
                    {
                        clearTesting();
                        break;
                    }
                }
        }

        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderClear(renderer);

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderCopy(renderer, message, NULL, &messageRect);
        SDL_Rect r;
        r.w = FACTOR;
        r.h = FACTOR;
        for(unsigned short y = 0; y < SIZE; y++)
        {
            for(unsigned short x = 0; x < SIZE; x++)
            {
                if(draw[y][x])
                {
                    r.x = FACTOR * x;
                    r.y = FACTOR * y;
                    SDL_RenderFillRect(renderer, &r);
                }
            }
        }

        for(unsigned short i = 0; i <= SIZE; i++)
        {
            SDL_RenderDrawLine(renderer, i * FACTOR, 0, i * FACTOR, FACTORxSIZE);
            SDL_RenderDrawLine(renderer, 0, i * FACTOR, FACTORxSIZE, i * FACTOR);
        }

        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
