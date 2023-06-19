#pragma once
#include "../state/state.hpp"

class AlphaBeta {
  public:
  static std::pair<Move, int> get_move(State *state, int alpha, int beta, int depth, bool maximizing_player);
};
