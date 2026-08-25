# Axis-overlap control — measurement procedure, fixed BEFORE any overlap was computed

Registered 2026-08-18, after axis P runs PO-1..5 / PS-2,3,5 returned but before any
cross-axis comparison was made. The proposal named the threshold (>90% = axes not distinct)
but not the procedure; the procedure is pinned here so it cannot be chosen to fit the answer.

## Why not leaf-name overlap
Leaves are named in the vocabulary of their own axis. Name matching would return ~0 overlap
for any pair of axes and would pass the control automatically, i.e. measure nothing.
Semantic leaf matching needs a judge over ~130x2 leaves per pair - a new sensor with its own bias.

## The procedure adopted
Compare the two axes through the common substrate the proposal already names: the fixed
list of RFP requirements.
1. Fix the requirement list from the RFP digest (functional + non-functional), one entry per
   named obligation. Same list for both axes.
2. For each tree, map every leaf to the requirement(s) it covers. This yields, per axis,
   a mapping requirement -> set of leaves, and hence a PARTITION of the requirement list
   induced by which leaves co-occur.
3. Overlap = agreement between the two induced partitions of the SAME requirement list.
4. >90% agreement => the axes cut the requirements along the same boundaries => not distinct
   => the experiment did not happen and nothing else is read.

## Cost, stated in advance
This measures similarity of PARTITIONS, not similarity of leaves. It will read systematically
lower than a naive leaf-list overlap. The 90% threshold was named before any metric existed,
so it is not calibrated to this metric either way - noted, not adjusted.
