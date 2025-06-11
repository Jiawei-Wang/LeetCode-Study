1. ml objective: maximize number of connections between users
2. input and output: user -> list of connections ranked by relevance
3. ml category: Learning to Rank with social graph as input
4. data: users, connections, interactions
5. model: Graph Neural Net -> predict if an edge (connection) exists between nodes (users)
   1. graph as input (nodes have information about users, edges have information about user-user characteristics)
   2. node embeddings for each node as output
   3. dot product between two embeddings for edge prediction
6. training dataset: snapshot of graph, node features and edge features, labels
7. evaluation
   offline: ROC-AUC
   online: number of new connections 
8. serving 
   1. handle too many nodes and edges: rule based filter + online prediction only for active users + scheduled batch prediction update
   2. generation pipeline: database -> feature computation -> rule based filter -> candidate users -> GNN -> score -> batch prediction db
   3. prediction pipeline: if in db -> fetch, if not -> new request to generation pipeline