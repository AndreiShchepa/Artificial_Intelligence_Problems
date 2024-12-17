# Web Crawling Algorithm Project Report

## Problem Statement

The program's input consists of URLs from two prestigious computer science schools' websites, for example, `www.fit.cvut.cz` and `www.mit.edu`. The task is to design an algorithm that finds a path through internet links from one input website to the other.

## Approach and Iterations

### 1. Bidirectional Search (BS)

My initial approach was to implement Bidirectional Search, as we have 1 start state and 1 final state. However, after the first run, which found a path through `https://youtube.com/about`, it became clear that something was amiss. Upon investigation, I realized that the existence of a link from A to B doesn't necessarily imply a link from B to A. This realization prompted me to seek an alternative solution.

### 2. Breadth-First Search (BFS) and Depth-Limited Search (DLS)

Next, I considered two other algorithms: Breadth-First Search (BFS) and Depth-Limited Search (DLS). I was hesitant about DLS, even with a depth limit, due to the vast scale of the network. There was a risk of either taking an infinite (infinite ~ too much) amount of time to find the final node or potentially missing the solution if the depth limit wasn't chosen correctly.

BFS seemed more reliable, so I implemented and ran the algorithm. After `2 hours`, I had to terminate the program and reassess my approach. Further investigation revealed that a single page often contains from `1 to 200` links. At a depth of 5, this could potentially mean traversing ~ 80^4 websites. If the possible path from website A to B involves 10 links (probably more), the time complexity becomes unmanageable. Moreover, using recursion would likely lead to a call stack limit error.

### 3. Intelligent Limitations and Heuristics

Recognizing that simple, non-intelligent methods were insufficient, I decided to introduce limitations and heuristics to make the algorithm more intelligent and increase the probability of finding a solution in a reasonable timeframe.

#### Data Cleaning:
- Remove "www" from the beginning of URLs and use "http" instead of "https" to eliminate redundant traversing.

#### Limitations:
- Exclude links to files (e.g., PDF, PHP) as they're unlikely to contain relevant information for our path.
- Avoid processing links to social media main pages (e.g., **facebook.com**, **youtube.com**, and bunch of others) to get rid of unnecessary millions of links.
- Ignore paths that are unlikely to lead to the final state, such as **registration**, **about**, and other similar pages.

#### Heuristics:
1. `URL Similarity`: Prefer links more similar to our target URL based on the following discussion on stackoverflow: https://stackoverflow.com/questions/73273671/how-to-check-the-similarity-score-between-two-web-urls
2. `Depth Control`: Implement a mechanism to backtrack if a certain depth is reached without finding the result.
3. `Domain Rewards`: Prioritize links with different Top-Level Domains (TLDs) from initial to encourage exploration.
4. `Path Length Penalty`: Penalize very long paths, as shorter paths are more likely to contain external links and general information.

## Results

`!IMPORTANT!` - This algorithm can guarantee neither a solution (due to the limited maximum depth) nor an optimal solution (as it stops at the first solution found and uses non-admissible heuristics).

After implementing these improvements, I ran the program with a maximum depth of 20. It found a solution in 7 minutes - a significant improvement over the initial attempts:

 - www.fit.cvut.cz -> http://klubfitpp.cz -> http://seznamovak.fit.cvut.cz -> http://suse.com -> http://opensuse.org -> http://planet.opensuse.org -> http://planet.kde.org -> http://volkerkrause.eu -> http://unifiedpush.org -> http://ngi.eu -> http://ngi.eu/ngi-projects -> http://ngi.eu/ngi-projects/elitr -> http://isl.anthropomatik.kit.edu/english -> http://cs.cmu.edu -> http://cs.cmu.edu/events/scs-seminar-series -> http://cs.cmu.edu/~aiseminar -> http://xiangxiangxu.mit.edu -> http://web.mit.edu -> www.mit.edu
