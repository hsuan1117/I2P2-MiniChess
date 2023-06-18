#include "MiniMax.hpp"
#include "../state/state.hpp"
#include <cstdlib>

using namespace std;
#define mp std::make_pair

/**
 * @brief Get a legal action using MiniMax algorithm
 *
 * @param state Now state
 * @param depth You may need this for other policy
 * @return <Move, value>
 */
std::pair<Move, int> MiniMax::get_move(State *state, int alpha, int beta, int depth, bool maximizing_player) {
  if (depth == 0 || state->legal_actions.empty()) {
    return mp(mp(mp(-1, -1), mp(-1, -1)), state->evaluate() * (maximizing_player ? 1 : -1));
  }

  if (maximizing_player) {
    // when it's player, pick the largest score
    int value = -INT_MAX;
    Move move;
    for (auto action: state->legal_actions) {
      auto next_state = state->next_state(action);
      auto next_move = get_move(next_state, alpha, beta, depth - 1, false);
      if (next_move.second > value) {
        value = next_move.second;
        move = action;
      }
      alpha = max(alpha, value);
      if (beta <= alpha)
        break;
    }
    return mp(move, value);
  } else {
    // when it's opponent, pick the smallest score
    int value = INT_MAX;
    Move move;
    for (auto action: state->legal_actions) {
      auto next_state = state->next_state(action);
      auto next_move = get_move(next_state, alpha, beta, depth - 1, true);
      if (next_move.second < value) {
        value = next_move.second;
        move = action;
      }
      beta = min(beta, value);
      if (beta <= alpha)
        break;
    }
    return mp(move, value);
  }
}