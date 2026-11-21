"""Execute representative pedagogical examples, not just the problem bank."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def study_module(level, name):
    path = ROOT / 'lessons' / level / name
    content = path.read_text(encoding='utf-8')
    namespace = {}
    for snippet in re.findall(r'```python\n(.*?)\n```', content, re.S):
        exec(compile(snippet, str(path), 'exec'), namespace)
    return namespace


class MasteryWorkedExampleTests(unittest.TestCase):
    def test_arrays_and_recursion(self):
        a = study_module('basics', '06_arrays_strings_and_index_invariants.md')
        self.assertEqual(a['move_zeros']([0,4,0,5,7]), [4,5,7,0,0])
        self.assertEqual(a['common_prefix'](['flower','flow','flight']), 'fl')
        r = study_module('basics', '07_recursion_call_stack_and_base_cases.md')
        self.assertEqual(r['fib'](10), 55)
        self.assertEqual(len(r['subsets']([1,2,3])), 8)
        self.assertEqual(len(r['subsets']([])), 1)

    def test_linked_list_queue_and_bit_set(self):
        l = study_module('basics','08_linked_lists_and_pointer_mutation.md')
        head = l['Node'](1, l['Node'](2, l['Node'](3)))
        reversed_head = l['reverse'](head)
        values = []
        while reversed_head:
            values.append(reversed_head.value)
            reversed_head = reversed_head.next
        self.assertEqual(values, [3,2,1])
        q = study_module('basics', '09_queues_deques_and_bfs_frontiers.md')
        self.assertEqual(q['shortest_unweighted']({'a':['b','c'],'b':['d']},'a')['d'], 2)
        self.assertEqual(q['window_max']([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        b = study_module('basics','11_bits_integer_arithmetic_and_overflow.md')
        self.assertTrue(b['unique_lowercase_letters']('abc'))
        self.assertFalse(b['unique_lowercase_letters']('abca'))
        self.assertEqual(b['singleton']([2,9,2]), 9)
        self.assertEqual(b['bit_count_positive'](13), 3)

    def test_intermediate_patterns(self):
        m = study_module('intermediate', '05_monotonic_stacks_and_deques.md')
        self.assertEqual(m['days_until_higher']([70,73,72,80]), [1,2,1,0])
        self.assertEqual(m['max_windows']([2,1,4,3],2), [2,4,4])
        search = study_module('intermediate','06_binary_search_on_answer_and_boundary_predicates.md')
        self.assertEqual(search['minimize_largest_day']([7,2,5,10,8],2), 18)
        heap = study_module('intermediate', '08_heaps_selection_and_top_k.md')
        self.assertEqual(heap['kth_distinct']([4,7,7,3,9],2), 7)
        greedy = study_module('intermediate','09_greedy_algorithms_and_exchange_arguments.md')
        self.assertEqual(len(greedy['max_nonoverlapping']([(1,4),(4,7),(3,5)])), 2)
        queens = study_module('intermediate','11_backtracking_pruning_and_state_restoration.md')
        self.assertEqual(len(queens['queens'](4)), 2)
        select = study_module('intermediate', '12_algorithm_selection_and_constraint_drills.md')
        self.assertEqual(select['count_target_ranges']([1,-1,0],0), 3)

    def test_advanced_algorithms(self):
        paths = study_module('advanced','05_shortest_paths_and_weight_assumptions.md')
        edges = [(0,1,5),(0,2,1),(2,1,1),(1,3,2)]
        self.assertEqual(paths['dijkstra'](4,edges,0),[0,2,1,4])
        bf,neg = paths['bellman_ford'](4,edges,0)
        self.assertEqual(bf,[0,2,1,4]);self.assertFalse(neg)
        t = study_module('advanced','06_topological_sort_scc_and_dependency_cycles.md')
        self.assertEqual(t['topo_lexicographic'](4,[(0,2),(1,2),(2,3)]),[0,1,2,3])
        self.assertEqual(t['topo_lexicographic'](2,[(0,1),(1,0)]),[])
        dp = study_module('advanced','07_dp_multidimensional_state_design.md')
        self.assertEqual(dp['edit_distance']('horse','ros'),3)
        opt = study_module('advanced','08_dp_optimization_and_space_compression.md')
        self.assertEqual(opt['edit_distance_rolling']('horse','ros'),3)
        self.assertEqual(opt['knapsack_01']([(2,3)],4),3)
        self.assertEqual(opt['lis_length']([3,5,1,2,8]),3)
        bit = study_module('advanced','09_fenwick_segment_trees_and_range_queries.md')
        fenwick = bit['Fenwick'](4)
        for i,x in enumerate([3,1,4,1]): fenwick.add(i,x)
        self.assertEqual(fenwick.range_sum(1,4),6)
        fenwick.add(2,5)
        self.assertEqual(fenwick.range_sum(1,4),11)
        d = study_module('advanced','10_amortized_analysis_dsu_and_rollback.md')['DSU'](4)
        d.union(0,1);d.union(2,3)
        self.assertNotEqual(d.find(0),d.find(3))
        d.union(1,2)
        self.assertEqual(d.find(0),d.find(3))
        s = study_module('advanced','12_mini_system_design_algorithm_capstone.md')
        self.assertEqual(s['schedule']([3,2,4,1],[(0,2),(1,2),(2,3)]),
                         ([0,1,2,3],[0,0,3,7],[3,2,7,8],8))


if __name__ == '__main__':
    unittest.main()
