import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int index;
        int distance;

        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.distance, other.distance);
        }
    }

    public static void dijkstra(int k, List<List<Node>> graph, int[] visited) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(k, 0));
        visited[k] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.index;
            int dist = node.distance;

            if (visited[now] < dist) {
                continue;
            }

            for (Node adjacent : graph.get(now)) {
                int newDist = dist + adjacent.distance;
                if (newDist < visited[adjacent.index]) {
                    visited[adjacent.index] = newDist;
                    pq.offer(new Node(adjacent.index, newDist));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int V = scanner.nextInt();
        int E = scanner.nextInt();
        int k = scanner.nextInt();

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= V; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            int u = scanner.nextInt();
            int v = scanner.nextInt();
            int w = scanner.nextInt();
            graph.get(u).add(new Node(v, w));
        }

        int[] visited = new int[V + 1];
        Arrays.fill(visited, Integer.MAX_VALUE);

        dijkstra(k, graph, visited);

        for (int i = 1; i <= V; i++) {
            if (visited[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(visited[i]);
            }
        }
    }
}