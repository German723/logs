# questions

1. 新建表格后如何查询信息

Execution Plan
----------------------------------------------------------
Plan hash value: 843138903

--------------------------------------------------------------------------------
-----------------------------

| Id  | Operation			  | Name		    | Rows  | By
tes | Cost (%CPU)| Time     |

--------------------------------------------------------------------------------
-----------------------------

|   0 | SELECT STATEMENT		  |			    |	  1 |
122 |	114   (1)| 00:00:02 |

|*  1 |  FILTER 			  |			    |	    |
    |		 |	    |

|   2 |   NESTED LOOPS			  |			    |	  2 |
244 |	114   (1)| 00:00:02 |

|*  3 |    HASH JOIN			  |			    |	  2 |
210 |	112   (1)| 00:00:02 |

|*  4 |     TABLE ACCESS BY INDEX ROWID   | OBJ$		    |	  2 |
166 |	110   (0)| 00:00:02 |

|*  5 |      INDEX SKIP SCAN		  | I_OBJ2		    |	  2 |
    |	108   (0)| 00:00:02 |

|   6 |     INDEX FULL SCAN		  | I_USER2		    |	 93 |  2
046 |	  1   (0)| 00:00:01 |

|   7 |    TABLE ACCESS CLUSTER 	  | USER$		    |	  1 |
 17 |	  1   (0)| 00:00:01 |

|*  8 |     INDEX UNIQUE SCAN		  | I_USER#		    |	  1 |
    |	  0   (0)| 00:00:01 |

|*  9 |   TABLE ACCESS BY INDEX ROWID	  | IND$		    |	  1 |
  8 |	  2   (0)| 00:00:01 |

|* 10 |    INDEX UNIQUE SCAN		  | I_IND1		    |	  1 |
    |	  1   (0)| 00:00:01 |

|* 11 |   HASH JOIN			  |			    |	  1 |
 24 |	  3  (34)| 00:00:01 |

|* 12 |    INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
 11 |	  2   (0)| 00:00:01 |

|  13 |    FIXED TABLE FULL		  | X$KZSRO		    |	100 |  1
300 |	  0   (0)| 00:00:01 |

|* 14 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 15 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  16 |   NESTED LOOPS			  |			    |	  2 |
 48 |	  2   (0)| 00:00:01 |

|* 17 |    INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
 11 |	  2   (0)| 00:00:01 |

|* 18 |    FIXED TABLE FULL		  | X$KZSRO		    |	  2 |
 26 |	  0   (0)| 00:00:01 |

|* 19 |   HASH JOIN			  |			    |	  1 |
 24 |	  3  (34)| 00:00:01 |

|* 20 |    INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
 11 |	  2   (0)| 00:00:01 |

|  21 |    FIXED TABLE FULL		  | X$KZSRO		    |	100 |  1
300 |	  0   (0)| 00:00:01 |

|* 22 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  23 |   NESTED LOOPS			  |			    |	    |
    |		 |	    |

|  24 |    NESTED LOOPS 		  |			    |	  1 |
 78 |	  7   (0)| 00:00:01 |

|  25 |     NESTED LOOPS		  |			    |	  1 |
 68 |	  5   (0)| 00:00:01 |

|  26 |      NESTED LOOPS		  |			    |	  1 |
 57 |	  4   (0)| 00:00:01 |

|  27 |       MERGE JOIN CARTESIAN	  |			    |	  1 |
 53 |	  3   (0)| 00:00:01 |

|* 28 |        INDEX RANGE SCAN 	  | I_OBJ5		    |	  1 |
 40 |	  3   (0)| 00:00:01 |

|  29 |        BUFFER SORT		  |			    |	100 |  1
300 |	  0   (0)| 00:00:01 |

|  30 | 	FIXED TABLE FULL	  | X$KZSRO		    |	100 |  1
300 |	  0   (0)| 00:00:01 |

|* 31 |       INDEX RANGE SCAN		  | I_USER2		    |	  1 |
  4 |	  1   (0)| 00:00:01 |

|* 32 |      INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
 11 |	  1   (0)| 00:00:01 |

|* 33 |     INDEX RANGE SCAN		  | I_DEPENDENCY1	    |	  3 |
    |	  1   (0)| 00:00:01 |

|* 34 |    TABLE ACCESS BY INDEX ROWID	  | DEPENDENCY$ 	    |	  1 |
 10 |	  2   (0)| 00:00:01 |

|* 35 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  36 |   NESTED LOOPS			  |			    |	  2 |
 76 |	  3   (0)| 00:00:01 |

|  37 |    NESTED LOOPS 		  |			    |	  1 |
 25 |	  3   (0)| 00:00:01 |

|* 38 |     TABLE ACCESS BY INDEX ROWID   | TRIGGER$		    |	  1 |
 14 |	  2   (0)| 00:00:01 |

|* 39 |      INDEX UNIQUE SCAN		  | I_TRIGGER2		    |	  1 |
    |	  1   (0)| 00:00:01 |

|* 40 |     INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
 11 |	  1   (0)| 00:00:01 |

|* 41 |    FIXED TABLE FULL		  | X$KZSRO		    |	  2 |
 26 |	  0   (0)| 00:00:01 |

|* 42 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  43 |   NESTED LOOPS			  |			    |	    |
    |		 |	    |

|  44 |    NESTED LOOPS 		  |			    |	  1 |
 78 |	  7   (0)| 00:00:01 |

|  45 |     NESTED LOOPS		  |			    |	  1 |
 68 |	  5   (0)| 00:00:01 |

|  46 |      NESTED LOOPS		  |			    |	  1 |
 57 |	  4   (0)| 00:00:01 |

|  47 |       MERGE JOIN CARTESIAN	  |			    |	  1 |
 53 |	  3   (0)| 00:00:01 |

|* 48 |        INDEX RANGE SCAN 	  | I_OBJ5		    |	  1 |
 40 |	  3   (0)| 00:00:01 |

|  49 |        BUFFER SORT		  |			    |	100 |  1
300 |	  0   (0)| 00:00:01 |

|  50 | 	FIXED TABLE FULL	  | X$KZSRO		    |	100 |  1
300 |	  0   (0)| 00:00:01 |

|* 51 |       INDEX RANGE SCAN		  | I_USER2		    |	  1 |
  4 |	  1   (0)| 00:00:01 |

|* 52 |      INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
 11 |	  1   (0)| 00:00:01 |

|* 53 |     INDEX RANGE SCAN		  | I_DEPENDENCY1	    |	  3 |
    |	  1   (0)| 00:00:01 |

|* 54 |    TABLE ACCESS BY INDEX ROWID	  | DEPENDENCY$ 	    |	  1 |
 10 |	  2   (0)| 00:00:01 |

|* 55 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 56 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 57 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 58 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 59 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 60 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 61 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 62 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 63 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 64 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 65 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 66 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 67 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 68 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 69 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 70 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 71 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 72 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 73 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 74 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|* 75 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  76 |   VIEW				  |			    |	  1 |
 13 |	  2   (0)| 00:00:01 |

|  77 |    FAST DUAL			  |			    |	  1 |
    |	  2   (0)| 00:00:01 |

|  78 |   NESTED LOOPS			  |			    |	  1 |
 21 |	  2   (0)| 00:00:01 |

|* 79 |    INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
  8 |	  2   (0)| 00:00:01 |

|* 80 |    FIXED TABLE FULL		  | X$KZSRO		    |	  1 |
 13 |	  0   (0)| 00:00:01 |

|* 81 |   FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  82 |   NESTED LOOPS			  |			    |	  1 |
 21 |	  2   (0)| 00:00:01 |

|* 83 |    INDEX RANGE SCAN		  | I_OBJAUTH1		    |	  1 |
  8 |	  2   (0)| 00:00:01 |

|* 84 |    FIXED TABLE FULL		  | X$KZSRO		    |	  1 |
 13 |	  0   (0)| 00:00:01 |

|* 85 |     FIXED TABLE FULL		  | X$KZSPR		    |	  1 |
 26 |	  0   (0)| 00:00:01 |

|  86 |   VIEW				  |			    |	  1 |
 16 |	  1   (0)| 00:00:01 |

|  87 |    SORT GROUP BY		  |			    |	  1 |
 86 |	  1   (0)| 00:00:01 |

|  88 |     NESTED LOOPS		  |			    |	  1 |
 86 |	  1   (0)| 00:00:01 |

|  89 |      MERGE JOIN CARTESIAN	  |			    |	  1 |
 78 |	  0   (0)| 00:00:01 |

|  90 |       NESTED LOOPS		  |			    |	  1 |
 65 |	  0   (0)| 00:00:01 |

|* 91 |        INDEX UNIQUE SCAN	  | I_OLAP_CUBES$	    |	  1 |
 13 |	  0   (0)| 00:00:01 |

|* 92 |        TABLE ACCESS BY INDEX ROWID| OLAP_DIMENSIONALITY$    |	  1 |
 52 |	  0   (0)| 00:00:01 |

|* 93 | 	INDEX RANGE SCAN	  | I_OLAP_DIMENSIONALITY$  |	  1 |
    |	  0   (0)| 00:00:01 |

|  94 |       BUFFER SORT		  |			    |	  1 |
 13 |	  0   (0)| 00:00:01 |

|  95 |        INDEX FULL SCAN		  | I_OLAP_CUBE_DIMENSIONS$ |	  1 |
 13 |	  0   (0)| 00:00:01 |

|* 96 |      INDEX RANGE SCAN		  | I_OBJ1		    |	  1 |
  8 |	  1   (0)| 00:00:01 |

|  97 |   NESTED LOOPS			  |			    |	  1 |
 29 |	  2   (0)| 00:00:01 |

|* 98 |    INDEX FULL SCAN		  | I_USER2		    |	  1 |
 20 |	  1   (0)| 00:00:01 |

|* 99 |    INDEX RANGE SCAN		  | I_OBJ4		    |	  1 |
  9 |	  1   (0)| 00:00:01 |

--------------------------------------------------------------------------------
-----------------------------


Predicate Information (identified by operation id):
---------------------------------------------------

   1 - filter(("O"."TYPE#"<>1 AND "O"."TYPE#"<>10 OR "O"."TYPE#"=1 AND	(SELECT
1 FROM "SYS"."IND$"

	      "I" WHERE "I"."OBJ#"=:B1 AND ("I"."TYPE#"=1 OR "I"."TYPE#"=2 OR "I
"."TYPE#"=3 OR "I"."TYPE#"=4 OR

	      "I"."TYPE#"=6 OR "I"."TYPE#"=7 OR "I"."TYPE#"=9))=1) AND (("O"."SP
ARE3"=USERENV('SCHEMAID') OR

	      "O"."SPARE3"=1) OR ("O"."TYPE#"=57 OR "O"."TYPE#"=69 OR "O"."TYPE#
"=72 OR "O"."TYPE#"=74 OR

	      "O"."TYPE#"=101) OR ("O"."TYPE#"=7 OR "O"."TYPE#"=8 OR "O"."TYPE#"
=9 OR "O"."TYPE#"=28 OR

	      "O"."TYPE#"=29 OR "O"."TYPE#"=30 OR "O"."TYPE#"=56) AND ( EXISTS (
SELECT 0 FROM "SYS"."OBJAUTH$"

	      "OA",SYS."X$KZSRO" "X$KZSRO" WHERE "OA"."GRANTEE#"="KZSROROL" AND
"OA"."OBJ#"=:B2 AND

	      ("OA"."PRIVILEGE#"=12 OR "OA"."PRIVILEGE#"=26)) OR  EXISTS (SELECT
 0 FROM SYS."X$KZSPR" "X$KZSPR"

	      WHERE "INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-144) OR (
-"KZSPRPRV")=(-141) OR

	      (-"KZSPRPRV")=(-241)))) OR ("O"."TYPE#"=1 OR "O"."TYPE#"=2 OR "O".
"TYPE#"=3 OR "O"."TYPE#"=4 OR

	      "O"."TYPE#"=5 OR "O"."TYPE#"=19 OR "O"."TYPE#"=20 OR "O"."TYPE#"=3
4 OR "O"."TYPE#"=35) AND  EXISTS

	      (SELECT 0 FROM SYS."X$KZSPR" "X$KZSPR" WHERE "INST_ID"=USERENV('IN
STANCE') AND ((-"KZSPRPRV")=(-45)

	      OR (-"KZSPRPRV")=(-47) OR (-"KZSPRPRV")=(-48) OR (-"KZSPRPRV")=(-4
9) OR (-"KZSPRPRV")=(-50))) OR

	      "O"."TYPE#"<>29 AND "O"."TYPE#"<>13 AND "O"."TYPE#"<>9 AND "O"."TY
PE#"<>11 AND "O"."TYPE#"<>30 AND

	      "O"."TYPE#"<>12 AND "O"."TYPE#"<>14 AND "O"."TYPE#"<>56 AND "O"."T
YPE#"<>8 AND "O"."TYPE#"<>7 AND

	      "O"."TYPE#"<>28 AND "O"."TYPE#"<>93 AND  EXISTS (SELECT 0 FROM "SY
S"."OBJAUTH$"

	      "OBJAUTH$",SYS."X$KZSRO" "X$KZSRO" WHERE "GRANTEE#"="KZSROROL" AND
 "OBJ#"=:B3 AND ("PRIVILEGE#"=3 OR

	      "PRIVILEGE#"=6 OR "PRIVILEGE#"=7 OR "PRIVILEGE#"=9 OR "PRIVILEGE#"
=10 OR "PRIVILEGE#"=11 OR

	      "PRIVILEGE#"=12 OR "PRIVILEGE#"=16 OR "PRIVILEGE#"=17 OR "PRIVILEG
E#"=18)) OR "O"."TYPE#"=13 AND (

	      EXISTS (SELECT 0 FROM "SYS"."OBJAUTH$" "OA",SYS."X$KZSRO" "X$KZSRO
" WHERE "OA"."GRANTEE#"="KZSROROL"

	      AND "OA"."OBJ#"=:B4 AND ("OA"."PRIVILEGE#"=12 OR "OA"."PRIVILEGE#"
=26)) OR  EXISTS (SELECT 0 FROM

	      SYS."X$KZSPR" "X$KZSPR" WHERE "INST_ID"=USERENV('INSTANCE') AND ((
-"KZSPRPRV")=(-184) OR

	      (-"KZSPRPRV")=(-181) OR (-"KZSPRPRV")=(-241)))) OR "O"."TYPE#"=11
AND ( EXISTS (SELECT 0 FROM

	      "SYS"."OBJAUTH$" "OA","SYS"."DEPENDENCY$" "DEP",SYS."USER$" "U",SY
S."OBJ$" "O",SYS."X$KZSRO"

	      "X$KZSRO" WHERE "O"."NAME"=:B5 AND "O"."SPARE3"=:B6 AND "O"."TYPE#
"=9 AND "O"."TYPE#"<>88 AND

	      "O"."OWNER#"="U"."USER#" AND "DEP"."D_OBJ#"=:B7 AND "DEP"."P_OBJ#"
="O"."OBJ#" AND

	      "OA"."OBJ#"="O"."OBJ#" AND "OA"."PRIVILEGE#"=26 AND "OA"."GRANTEE#
"="KZSROROL") OR  EXISTS (SELECT 0

	      FROM SYS."X$KZSPR" "X$KZSPR" WHERE ((-"KZSPRPRV")=(-141) OR (-"KZS
PRPRV")=(-241)) AND

	      "INST_ID"=USERENV('INSTANCE'))) OR "O"."TYPE#"=12 AND ( EXISTS (SE
LECT 0 FROM "SYS"."OBJAUTH$"

	      "OA","SYS"."TRIGGER$" "T",SYS."X$KZSRO" "X$KZSRO" WHERE "OA"."GRAN
TEE#"="KZSROROL" AND

	      "T"."OBJ#"=:B8 AND BITAND("T"."PROPERTY",24)=0 AND "OA"."OBJ#"="T"
."BASEOBJECT" AND

	      "OA"."PRIVILEGE#"=26) OR	EXISTS (SELECT 0 FROM SYS."X$KZSPR" "X$K
ZSPR" WHERE ((-"KZSPRPRV")=(-152)

	      OR (-"KZSPRPRV")=(-241)) AND "INST_ID"=USERENV('INSTANCE'))) OR "O
"."TYPE#"=14 AND ( EXISTS (SELECT

	      0 FROM "SYS"."OBJAUTH$" "OA","SYS"."DEPENDENCY$" "DEP",SYS."USER$"
 "U",SYS."OBJ$" "O",SYS."X$KZSRO"

	      "X$KZSRO" WHERE "O"."NAME"=:B9 AND "O"."SPARE3"=:B10 AND "O"."TYPE
#"=13 AND "O"."TYPE#"<>88 AND

	      "O"."OWNER#"="U"."USER#" AND "DEP"."D_OBJ#"=:B11 AND "DEP"."P_OBJ#
"="O"."OBJ#" AND

	      "OA"."OBJ#"="O"."OBJ#" AND "OA"."PRIVILEGE#"=26 AND "OA"."GRANTEE#
"="KZSROROL") OR  EXISTS (SELECT 0

	      FROM SYS."X$KZSPR" "X$KZSPR" WHERE ((-"KZSPRPRV")=(-181) OR (-"KZS
PRPRV")=(-241)) AND

	      "INST_ID"=USERENV('INSTANCE'))) OR "O"."TYPE#"=22 AND  EXISTS (SEL
ECT 0 FROM SYS."X$KZSPR" "X$KZSPR"

	      WHERE "INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-189) OR (
-"KZSPRPRV")=(-190) OR

	      (-"KZSPRPRV")=(-191) OR (-"KZSPRPRV")=(-192))) OR "O"."TYPE#"=6 AN
D  EXISTS (SELECT 0 FROM

	      SYS."X$KZSPR" "X$KZSPR" WHERE (-"KZSPRPRV")=(-109) AND "INST_ID"=U
SERENV('INSTANCE')) OR

	      "O"."TYPE#"=46 AND  EXISTS (SELECT 0 FROM SYS."X$KZSPR" "X$KZSPR"
W)

   3 - access("O"."OWNER#"="U"."USER#")
   4 - filter(BITAND("O"."FLAGS",128)=0)
   5 - access("O"."NAME"='tbl_objects' AND "O"."LINKNAME" IS NULL)
       filter("O"."NAME"='tbl_objects' AND "O"."NAME"<>'_NEXT_OBJECT' AND
	      "O"."NAME"<>'_default_auditing_options_' AND "O"."LINKNAME" IS NUL
L)

   8 - access("O"."SPARE3"="U"."USER#")
   9 - filter("I"."TYPE#"=1 OR "I"."TYPE#"=2 OR "I"."TYPE#"=3 OR "I"."TYPE#"=4 O
R "I"."TYPE#"=6 OR

	      "I"."TYPE#"=7 OR "I"."TYPE#"=9)
  10 - access("I"."OBJ#"=:B1)
  11 - access("OA"."GRANTEE#"="KZSROROL")
  12 - access("OA"."OBJ#"=:B1)
       filter("OA"."PRIVILEGE#"=12 OR "OA"."PRIVILEGE#"=26)
  14 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-144) OR (-"KZSP
RPRV")=(-141) OR

	      (-"KZSPRPRV")=(-241)))
  15 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-45) OR (-"KZSPR
PRV")=(-47) OR

	      (-"KZSPRPRV")=(-48) OR (-"KZSPRPRV")=(-49) OR (-"KZSPRPRV")=(-50))
)

  17 - access("OBJ#"=:B1)
       filter("PRIVILEGE#"=3 OR "PRIVILEGE#"=6 OR "PRIVILEGE#"=7 OR "PRIVILEGE#"
=9 OR

	      "PRIVILEGE#"=10 OR "PRIVILEGE#"=11 OR "PRIVILEGE#"=12 OR "PRIVILEG
E#"=16 OR "PRIVILEGE#"=17 OR

	      "PRIVILEGE#"=18)
  18 - filter("GRANTEE#"="KZSROROL")
  19 - access("OA"."GRANTEE#"="KZSROROL")
  20 - access("OA"."OBJ#"=:B1)
       filter("OA"."PRIVILEGE#"=12 OR "OA"."PRIVILEGE#"=26)
  22 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-184) OR (-"KZSP
RPRV")=(-181) OR

	      (-"KZSPRPRV")=(-241)))
  28 - access("O"."SPARE3"=:B1 AND "O"."NAME"=:B2 AND "O"."TYPE#"=9)
       filter("O"."TYPE#"=9 AND "O"."TYPE#"<>88)
  31 - access("O"."OWNER#"="U"."USER#")
  32 - access("OA"."OBJ#"="O"."OBJ#" AND "OA"."GRANTEE#"="KZSROROL" AND "OA"."PR
IVILEGE#"=26)

       filter("OA"."PRIVILEGE#"=26 AND "OA"."GRANTEE#"="KZSROROL")
  33 - access("DEP"."D_OBJ#"=:B1)
  34 - filter("DEP"."P_OBJ#"="O"."OBJ#")
  35 - filter(((-"KZSPRPRV")=(-141) OR (-"KZSPRPRV")=(-241)) AND "INST_ID"=USERE
NV('INSTANCE'))

  38 - filter(BITAND("T"."PROPERTY",24)=0)
  39 - access("T"."OBJ#"=:B1)
  40 - access("OA"."OBJ#"="T"."BASEOBJECT" AND "OA"."PRIVILEGE#"=26)
       filter("OA"."PRIVILEGE#"=26)
  41 - filter("OA"."GRANTEE#"="KZSROROL")
  42 - filter(((-"KZSPRPRV")=(-152) OR (-"KZSPRPRV")=(-241)) AND "INST_ID"=USERE
NV('INSTANCE'))

  48 - access("O"."SPARE3"=:B1 AND "O"."NAME"=:B2 AND "O"."TYPE#"=13)
       filter("O"."TYPE#"=13 AND "O"."TYPE#"<>88)
  51 - access("O"."OWNER#"="U"."USER#")
  52 - access("OA"."OBJ#"="O"."OBJ#" AND "OA"."GRANTEE#"="KZSROROL" AND "OA"."PR
IVILEGE#"=26)

       filter("OA"."PRIVILEGE#"=26 AND "OA"."GRANTEE#"="KZSROROL")
  53 - access("DEP"."D_OBJ#"=:B1)
  54 - filter("DEP"."P_OBJ#"="O"."OBJ#")
  55 - filter(((-"KZSPRPRV")=(-181) OR (-"KZSPRPRV")=(-241)) AND "INST_ID"=USERE
NV('INSTANCE'))

  56 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-189) OR (-"KZSP
RPRV")=(-190) OR

	      (-"KZSPRPRV")=(-191) OR (-"KZSPRPRV")=(-192)))
  57 - filter((-"KZSPRPRV")=(-109) AND "INST_ID"=USERENV('INSTANCE'))
  58 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-251) OR (-"KZSP
RPRV")=(-252) OR

	      (-"KZSPRPRV")=(-253) OR (-"KZSPRPRV")=(-254)))
  59 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-200) OR (-"KZSP
RPRV")=(-201) OR

	      (-"KZSPRPRV")=(-202) OR (-"KZSPRPRV")=(-203) OR (-"KZSPRPRV")=(-20
4)))

  60 - filter(((-"KZSPRPRV")=(-265) OR (-"KZSPRPRV")=(-266)) AND "INST_ID"=USERE
NV('INSTANCE'))

  61 - filter(((-"KZSPRPRV")=(-177) OR (-"KZSPRPRV")=(-178)) AND "INST_ID"=USERE
NV('INSTANCE'))

  62 - filter(((-"KZSPRPRV")=(-222) OR (-"KZSPRPRV")=(-223)) AND "INST_ID"=USERE
NV('INSTANCE'))

  63 - filter((-"KZSPRPRV")=12 AND "INST_ID"=USERENV('INSTANCE'))
  64 - filter((-"KZSPRPRV")=(-265) AND "INST_ID"=USERENV('INSTANCE'))
  65 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-45) OR (-"KZSPR
PRV")=(-47) OR

	      (-"KZSPRPRV")=(-48) OR (-"KZSPRPRV")=(-49) OR (-"KZSPRPRV")=(-50))
)

  66 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-205) OR (-"KZSP
RPRV")=(-206) OR

	      (-"KZSPRPRV")=(-207) OR (-"KZSPRPRV")=(-208)))
  67 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-258) OR (-"KZSP
RPRV")=(-259) OR

	      (-"KZSPRPRV")=(-260) OR (-"KZSPRPRV")=(-261)))
  68 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-246) OR (-"KZSP
RPRV")=(-247) OR

	      (-"KZSPRPRV")=(-248) OR (-"KZSPRPRV")=(-249)))
  69 - filter(((-"KZSPRPRV")=(-268) OR (-"KZSPRPRV")=(-267)) AND "INST_ID"=USERE
NV('INSTANCE'))

  70 - filter(((-"KZSPRPRV")=(-277) OR (-"KZSPRPRV")=(-278)) AND "INST_ID"=USERE
NV('INSTANCE'))

  71 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-292) OR (-"KZSP
RPRV")=(-293) OR

	      (-"KZSPRPRV")=(-294)))
  72 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-282) OR (-"KZSP
RPRV")=(-283) OR

	      (-"KZSPRPRV")=(-284) OR (-"KZSPRPRV")=(-285)))
  73 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-302) OR (-"KZSP
RPRV")=(-303) OR

	      (-"KZSPRPRV")=(-304) OR (-"KZSPRPRV")=(-305) OR (-"KZSPRPRV")=(-30
6) OR (-"KZSPRPRV")=(-307)))

  74 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-315) OR (-"KZSP
RPRV")=(-316) OR

	      (-"KZSPRPRV")=(-317) OR (-"KZSPRPRV")=(-318)))
  75 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-320) OR (-"KZSP
RPRV")=(-321) OR

	      (-"KZSPRPRV")=(-322)))
  79 - access("OBJ#"=:B1)
  80 - filter("GRANTEE#"="KZSROROL")
  81 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-309) OR (-"KZSP
RPRV")=(-310) OR

	      (-"KZSPRPRV")=(-311) OR (-"KZSPRPRV")=(-312) OR (-"KZSPRPRV")=(-31
3)))

  83 - access("OBJ#"=:B1)
  84 - filter("GRANTEE#"="KZSROROL")
  85 - filter("INST_ID"=USERENV('INSTANCE') AND ((-"KZSPRPRV")=(-302) OR (-"KZSP
RPRV")=(-303) OR

	      (-"KZSPRPRV")=(-304) OR (-"KZSPRPRV")=(-305) OR (-"KZSPRPRV")=(-30
6) OR (-"KZSPRPRV")=(-307)))

  91 - access("C"."OBJ#"=:B1)
  92 - filter("DIML"."DIMENSION_TYPE"=11)
  93 - access("DIML"."DIMENSIONED_OBJECT_ID"=:B1 AND "DIML"."DIMENSIONED_OBJECT_
TYPE"=1)

  96 - access("DIML"."DIMENSION_ID"="DO"."OBJ#")
       filter("DO"."OBJ#"="DIM"."OBJ#")
  98 - access("U2"."TYPE#"=2 AND "U2"."SPARE2"=TO_NUMBER(SYS_CONTEXT('userenv','
current_edition_id'))

	      )
       filter("U2"."TYPE#"=2 AND "U2"."SPARE2"=TO_NUMBER(SYS_CONTEXT('userenv','
current_edition_id'))

	      )
  99 - access("O2"."DATAOBJ#"=:B1 AND "O2"."TYPE#"=88 AND "O2"."OWNER#"="U2"."US
ER#")



Statistics
----------------------------------------------------------
	 29  recursive calls
	  0  db block gets
	 31  consistent gets
	  0  physical reads
	  0  redo size
	478  bytes sent via SQL*Net to client
	513  bytes received via SQL*Net from client
	  1  SQL*Net roundtrips to/from client
	  0  sorts (memory)
	  0  sorts (disk)
	  0  rows processed


