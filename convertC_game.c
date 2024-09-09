#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdbool.h>

#define SCREEN_WIDTH 1300
#define SCREEN_HEIGHT 700
#define DOT_SPEED -10
#define DOT_WIDTH 50
#define DOT_HEIGHT 50

// Dot 구조체 정의
typedef struct {
    SDL_Rect rect;
    int speed_x;
    int speed_y;
} Dot;

// 전역 변수 선언
SDL_Window* window = NULL;
SDL_Renderer* renderer = NULL;
SDL_Texture* dotTexture = NULL;
SDL_Texture* shapeTexture = NULL;
int score = 0;

// Dot 생성 함수
void initDot(Dot* dot) {
    dot->rect.x = SCREEN_WIDTH - DOT_WIDTH;
    dot->rect.y = SCREEN_HEIGHT / 2;
    dot->rect.w = DOT_WIDTH;
    dot->rect.h = DOT_HEIGHT;
    dot->speed_x = DOT_SPEED;
    dot->speed_y = 0;
}

// Dot 업데이트 함수
void updateDot(Dot* dot) {
    dot->rect.x += dot->speed_x;
    if (dot->rect.x < 100) {
        dot->rect.x = SCREEN_WIDTH;  // 화면 밖으로 나가면 오른쪽 끝으로 이동
    }
}

// Dot 그리기 함수
void renderDot(Dot* dot) {
    SDL_RenderCopy(renderer, dotTexture, NULL, &dot->rect);
}

int main(int argc, char* argv[]) {
    SDL_Init(SDL_INIT_VIDEO);

    // 윈도우 및 렌더러 생성
    window = SDL_CreateWindow("Rhythm Game", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    // 텍스처 로드
    SDL_Surface* dotSurface = SDL_LoadBMP("dot.bmp");
    dotTexture = SDL_CreateTextureFromSurface(renderer, dotSurface);
    SDL_FreeSurface(dotSurface);

    SDL_Surface* shapeSurface = SDL_LoadBMP("shape.bmp");
    shapeTexture = SDL_CreateTextureFromSurface(renderer, shapeSurface);
    SDL_FreeSurface(shapeSurface);

    bool quit = false;`
    SDL_Event e;
    Dot dot;
    initDot(&dot);
    Uint32 start_time = SDL_GetTicks();
    Uint32 current_time;
    Uint32 spawn_times[] = {3000, 3700, 4000, 4700, 5400, 5700, 6400, 6900, 7300, 7800};  // 시간 단위: 밀리초

    while (!quit) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }
        }

        // 시간 체크 및 Dot 업데이트
        current_time = SDL_GetTicks();
        for (int i = 0; i < sizeof(spawn_times) / sizeof(Uint32); ++i) {
            if (current_time >= start_time + spawn_times[i]) {
                updateDot(&dot);
                break;
            }
        }

        // 입력 처리
        const Uint8* state = SDL_GetKeyboardState(NULL);
        if (state[SDL_SCANCODE_SPACE]) {
            if (dot.rect.x >= 150 && dot.rect.x <= 250) {
                score++;
                initDot(&dot);  // 점수를 얻으면 Dot 다시 초기화
            }
        }

        // 화면 그리기
        SDL_RenderClear(renderer);
        renderDot(&dot);
        SDL_Rect shapeRect = {205, 395, DOT_WIDTH, DOT_HEIGHT};
        SDL_RenderCopy(renderer, shapeTexture, NULL, &shapeRect);

        // 점수 출력
        SDL_Color color = {0, 0, 0, 255};
        SDL_Surface* scoreSurface = SDL_CreateRGBSurface(0, 200, 100, 32, 0, 0, 0, 0);
        SDL_FillRect(scoreSurface, NULL, SDL_MapRGB(scoreSurface->format, color.r, color.g, color.b));
        SDL_Texture* scoreTexture = SDL_CreateTextureFromSurface(renderer, scoreSurface);
        SDL_FreeSurface(scoreSurface);
        SDL_RenderCopy(renderer, scoreTexture, NULL, NULL);
        SDL_DestroyTexture(scoreTexture);

        SDL_RenderPresent(renderer);
        SDL_Delay(16);  // 약 60 FPS
    }

    SDL_DestroyTexture(dotTexture);
    SDL_DestroyTexture(shapeTexture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
