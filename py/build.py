from neo4j import GraphDatabase
import json

# 连接到 Neo4j 数据库
uri = "bolt://localhost:7687"
username = "neo4j"
password = "txys66666"
driver = GraphDatabase.driver(uri, auth=(username, password))

# 读取 JSON 数据
with open("company_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 定义 Cypher 查询语句
cypher_create_node = """
    UNWIND $companies AS company
    CREATE (c:Company)
    SET c.name = company.name,
        c.type = company.type,
        c.size = company.size,
        c.address = company.address,
        c.founded = company.founded,
        c.business_area = company.business_area
"""

cypher_create_relationship = """
    UNWIND $relationships AS rel
    MATCH (source:Company {name: rel.source}), (target:Company {name: rel.target})
    CREATE (source)-[:HAS_RELATIONSHIP]->(target)
"""

# 执行 Cypher 查询
def execute_query(tx, cypher_query, data):
    tx.run(cypher_query, **data)

with driver.session() as session:
    session.write_transaction(execute_query, cypher_create_node, {"companies": data["companies"]})
    session.write_transaction(execute_query, cypher_create_relationship, {"relationships": data["relationships"]})

# 关闭数据库连接
driver.close()
