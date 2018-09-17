# -*- coding: utf-8 -*-
import pymysql
import json
import os

edge_sql_relation = """select source_user_id,target_user_id,trust_value from relationship where source_user_id=%s;"""
edge_sql_user = """select education,birthday,name,gender,hometown,language,work from user where id=%s;"""
fname = os.getcwd() + "/templates/user_data.json"


def init():
	conn = pymysql.connect(
			host = 'localhost',
			port = 3306,
			user = 'root',
			password = '111',
			charset ='utf8',
			db = 'social_networks')
	cursor = conn.cursor()
	return conn, cursor

def single1(conn, cursor, attr):
    js = {}
    edges, secondary_nodes, secondary_edges = [], [], []
    try:
        secondary_nodes.append(1)
        for node in secondary_nodes:
            sql = edge_sql_user % node
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                # secondary_edges.append({"source": node[1], "target": row[2], "relation": row[1], "label": row[3]})
                print("node:", node, "target:", row[0])
                secondary_edges.append({"source": node, "target": row[0], "relation": "education"})
                secondary_edges.append({"source": node, "target": row[1], "relation": "birthday"})
                secondary_edges.append({"source": node, "target": row[2], "relation": "name"})
                secondary_edges.append({"source": node, "target": row[3], "relation": "gender"})
                secondary_edges.append({"source": node, "target": row[4], "relation": "hometown"})
                secondary_edges.append({"source": node, "target": row[5], "relation": "language"})
                secondary_edges.append({"source": node, "target": row[6], "relation": "work"})
        print("secondary_edges", secondary_edges)
    except:
        conn.rollback()
    js["edges"] = edges
    js["secondary_edges"] = secondary_edges
    mydata = json.dumps(js, ensure_ascii=False).encode("utf8")
    with open(fname, 'wb+') as f:
        f.write(mydata)
        f.close()
    return mydata


def single(conn, cursor, attr):
    js = {}
    edges, secondary_nodes, secondary_edges = [], [], []
    try:
        sql = edge_sql_relation%attr
        print("sql :", sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print("friend:", row[1])
            secondary_nodes.append(row[1])
            #edges.append({"source": row[0], "target": row[1], "relation": "%s" % (row[2])})
        edges.append({"source": 2, "target": 12, "relation": "%s" % (0.92)})
        edges.append({"source": 2, "target": 13, "relation": "%s" % (0.87)})
        edges.append({"source": 2, "target": 14, "relation": "%s" % (0.93)})
        #edges.append({"source": 2, "target": 15, "relation": "%s" % (0.87)})


        edges.append({"source": 12, "target": 15, "relation": "%s" % (0.87)})
        edges.append({"source": 12, "target": 16, "relation": "%s" % (0.87)})
        #edges.append({"source": 7, "target": , "relation": "%s" % (0.87)})

        edges.append({"source": 13, "target": 17, "relation": "%s" % (0.87)})
        edges.append({"source": 13, "target": 18, "relation": "%s" % (0.87)})
        #edges.append({"source": 8, "target": 24, "relation": "%s" % (0.87)})

        edges.append({"source": 14, "target": 19, "relation": "%s" % (0.87)})
        edges.append({"source": 14, "target": 20, "relation": "%s" % (0.87)})
        #edges.append({"source": 12, "target": 27, "relation": "%s" % (0.87)})

        edges.append({"source": 1, "target": 15, "relation": "%s" % (0.87)})
        edges.append({"source": 1, "target": 16, "relation": "%s" % (0.87)})
        edges.append({"source": 1, "target": 17, "relation": "%s" % (0.87)})

        edges.append({"source": 1, "target": 18, "relation": "%s" % (0.87)})
        edges.append({"source": 1, "target": 19, "relation": "%s" % (0.87)})
        edges.append({"source": 1, "target": 20, "relation": "%s" % (0.87)})

    except:
        conn.rollback()
    js["edges"] = edges
    js["secondary_edges"] = secondary_edges
    mydata = json.dumps(js, ensure_ascii=False).encode("utf8")
    with open(fname, 'wb+') as f:
        f.write(mydata)
        f.close()
    return mydata

def execute(conn, cursor, attr):
    js = {}
    edges, secondary_nodes, secondary_edges = [], [], []
    try:
        sql = edge_sql_relation%attr
        print("sql :", sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        for row in results:
            print("好友：", row[1])
            secondary_nodes.append(row[1])
            sql1 = 'select name from user where id=%s'%row[1]
            cursor.execute(sql1)
            nikename = cursor.fetchall()[0][0]
            #edges.append({"source": "xlcheng", "target": row[5], "relation": row[2], "label": row[-1]})
            edges.append({"source": row[0], "target": row[1], "relation": "%s"%(row[2])})
        print("secondary_nodes:", secondary_nodes)
        #edges.append({"source":2, "target": 3, "relation": "%s,%s"%(1.0,1.0)})
        #edges.append({"source": 2, "target": 7, "relation": "%s,%s" % ("test","test")})
        #edges.append({"source": 1, "target": 7, "relation": "%s,%s" % ("test","test")})
        #edges.append({"source": 4, "target": 7, "relation": "%s,%s" % ("test","test")})
        #edges.append({"source": 5, "target": 7, "relation": "%s,%s" % ("test","test")})
        for node in secondary_nodes:
            sql = edge_sql_user%node
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                #secondary_edges.append({"source": node[1], "target": row[2], "relation": row[1], "label": row[3]})
                print("node:",node,"target:",row[0])
                secondary_edges.append({"source": node, "target":row[0], "relation": "education"})
                secondary_edges.append({"source": node, "target": row[1], "relation": "birthday"})
                secondary_edges.append({"source": node, "target": row[2], "relation": "name"})
                secondary_edges.append({"source": node, "target": row[3], "relation": "gender"})
                secondary_edges.append({"source": node, "target": row[4], "relation": "hometown"})
                secondary_edges.append({"source": node, "target": row[5], "relation": "language"})
                secondary_edges.append({"source": node, "target": row[6], "relation": "work"})
        print("secondary_edges", secondary_edges)
    except:
        conn.rollback()
    js["edges"] = edges
    js["secondary_edges"] = secondary_edges
    mydata = json.dumps(js, ensure_ascii=False).encode("utf8")
    with open(fname, 'wb+') as f:
        f.write(mydata)
        f.close()
    return mydata