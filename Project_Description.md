# Chameleon Game

---

## Core Design Principles

- The `GameController` is the permanent, neutral host by default
- A human player can take the host role and replace the `GameController` entirely for that match
- All decisions (mode selection, eliminations, awards) are resolved by majority vote
- Words and topics are always computer-generated
- New modes and roles can be added without changing existing code
- Rooms persist across matches, keeping history and leaderboards intact

---

## Modules

### User Management
- Stores username, password, and profile
- Profile tracks global stats, per-room stats, and match history

### Room System
- Has a unique ID and access code
- Holds a member list, match history, and a leaderboard
- Creates and stores matches

### Game Controller
- Runs mode voting, role assignment, rounds, elimination voting, and award voting
- Logs the match and updates all stats when done
- Can be replaced by a human host for a given match

### Human Host
- Takes over from the `GameController` for that match only
- Manually selects the game mode
- Manually assigns roles (Imposter, Jester, etc.) or uses random assignment
- All other match logic (rounds, turns, voting, logging) continues as normal

### Match
- Holds the chosen mode, player list, rounds, game state, and final result

### Rounds and Turns
- A round runs one cycle of play for all active players
- A turn stores one player's response and locks after submission
- Each match has 1+ rounds; each round has 1 turn per player

### Game Modes
All modes implement the `GameMode` interface.

| Mode | Description |
|---|---|
| `ImposterMode` | One imposter, rest are majority players |
| `ImposterJesterMode` | Adds a Jester who wins by getting voted out |
| `ApplesPearsMode` | Only one player receives a slightly different word and tries to blend in |
| `SurpriseMode` | Randomly picks one of the other modes at runtime |

### Roles
All roles implement the `Role` interface.

| Role | Win Condition |
|---|---|
| `MajorityRole` | Vote out the imposter |
| `ImposterRole` | Avoid detection and survive, or guess the word on their turn |
| `JesterRole` | Get voted out by the majority |

### Voting System
All strategies implement `VotingStrategy`.

| Strategy | Used For |
|---|---|
| `ModeVoting` | Choosing the game mode |
| `EliminationVoting` | Voting a player out |
| `AwardVoting` | Post-match award selection |

### Word Provider
- `AutoWordProvider` generates a topic and player words based on the active mode
- Will be implemented by SAT

### Award System
Post-match awards voted on by players.

| Award | Given To |
|---|---|
| GOATED | Best overall performance |
| GENERALIST | Most adaptable across roles |
| AARONIC | Most Aaronic moment |

### Reconnection Handler
- Detects disconnect and starts a grace period
- Allows rejoin without disrupting the match

### Analytics and Leaderboard
- Tracks wins, losses, awards, imposter success rate, and turn duration per player
- Room leaderboard updates after every match

---

## System Relationships

```
User ──────────── Profile
User ──────────── Room (many-to-many)
Room ──────────── Match (1-to-many)
Match ─────────── Round (1-to-many)
Round ─────────── Turn (1-to-many)
Match ─────────── GameMode
Match ─────────── GameState
Match ─────────── MatchResult
GameController ── Match
HumanHost ──────── Match (replaces GameController per match)
GameController ── VotingStrategy (interface)
GameController ── WordProvider (interface)
GameController ── AwardStrategy (interface)
GameController ── ReconnectHandler (interface)
GameController ── AnalyticsService (interface)
SurpriseMode ──── GameMode (delegation)
```

---

## Design Patterns

| Pattern | Where |
|---|---|
| Strategy | `VotingStrategy`, `AwardStrategy` |
| Interface / Polymorphism | `GameMode`, `Role`, `Host` |
| Dependency Inversion | `GameController` depends only on interfaces |
| Composition | `Match` owns `Round`s; `Round` owns `Turn`s |
| Delegation | `SurpriseMode` passes control to another `GameMode` |

---