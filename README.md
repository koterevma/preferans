## Задача

В колоде 32 карты. Чтобы определить кто ходит первым, игрокам по очереди выдают по карте рубашкой вверх,
затем переворачивают. Первым ходит тот, кто первый возьмет шестерку

## Код

В [main.py](./main.py) приведена программа, которая эмулирует N (EMULATE_COUNT) раздач

Раздачу начинают с игрока m (PLAYER_START)

Результатом работы программы является расчитанные вероятности того, какой игрок ходит первым

## Примеры запусков

```
PLAYERS_COUNT=3; PLAYER_START=0; EMULATE_COUNT=1000000
Player 0 selected 373283 times. Probability is 0.373
Player 1 selected 331824 times. Probability is 0.332
Player 2 selected 294893 times. Probability is 0.295
```

```
PLAYERS_COUNT=3; PLAYER_START=1; EMULATE_COUNT=1000000
Player 0 selected 294795 times. Probability is 0.295
Player 1 selected 372934 times. Probability is 0.373
Player 2 selected 332271 times. Probability is 0.332
```

```
PLAYERS_COUNT=3; PLAYER_START=2; EMULATE_COUNT=1000000
Player 0 selected 332004 times. Probability is 0.332
Player 1 selected 295416 times. Probability is 0.295
Player 2 selected 372580 times. Probability is 0.373
```

```
PLAYERS_COUNT=2; PLAYER_START=0; EMULATE_COUNT=1000000
Player 0 selected 528808 times. Probability is 0.529
Player 1 selected 471192 times. Probability is 0.471
```

```
PLAYERS_COUNT=5; PLAYER_START=0; EMULATE_COUNT=1000000
Player 0 selected 249238 times. Probability is 0.249
Player 1 selected 222231 times. Probability is 0.222
Player 2 selected 197315 times. Probability is 0.197
Player 3 selected 176476 times. Probability is 0.176
Player 4 selected 154740 times. Probability is 0.155
```

```
PLAYERS_COUNT=5; PLAYER_START=2; EMULATE_COUNT=1000000
Player 0 selected 176011 times. Probability is 0.176
Player 1 selected 155687 times. Probability is 0.156
Player 2 selected 248270 times. Probability is 0.248
Player 3 selected 222211 times. Probability is 0.222
Player 4 selected 197821 times. Probability is 0.198
```

## Вывод

Благодаря эмуляции достаточно большого числа раздач можно убедиться,
что вероятность того, что игрок будет ходить первым будет зависить от
того, с какого игрока начиналась раздача. Причем она тем больше, чем раньше
игрок получит свою первую карту
