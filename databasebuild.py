from dis import Instruction
import sqlite3 as sql

def createDB():
    conn = sql.connect("personajes.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("personajes.db")
    cursor = conn.cursor()
    cursor.execute(
        """Create table personajes (
            name text,
            difference text
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre, diferiencia):
    conn = sql.connect("personajes.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO personajes VALUES ('{nombre}', '{diferiencia}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def readRow():
    conn = sql.connect("personajes.db")
    cursor = conn.cursor()
    instruction = f"SELCT * FROM personajes"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

def updateFields():
    conn = sql.connect("personajes.db")
    cursor = conn.cursor()
    instruction = f"UPDATE personajes SET name='Aragorn' WHERE name like 'boromir'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createDB()
    #createTable()
    #inserRow("Aragorn", "es un montaraz")
    readRow()
    #updateFields()