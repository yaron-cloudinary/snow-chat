
# PROMPT
```
 who are the customers that their mrr changed to 0 and previous month was >0. Don't use UPDATED_ATS, LAST_MRR_DOLLAR. limit to 10 top ones 
```


# SQL
```sql
 SELECT
    NAME,
    SALESFORCE_ID,
    EXTERNAL_ID,
    MRR_DOLLAR,
    LAST_MONTH_MRR_DOLLAR
FROM
    dim.accounts
WHERE
    MRR_DOLLAR = 0
    AND LAST_MONTH_MRR_DOLLAR > 0
ORDER BY
    LAST_MONTH_MRR_DOLLAR DESC
LIMIT 10; 
```


# DATA
| NAME                   | SALESFORCE_ID      | EXTERNAL_ID                          |   MRR_DOLLAR |   LAST_MONTH_MRR_DOLLAR |
|------------------------|--------------------|--------------------------------------|--------------|-------------------------|
| Media Ocean- Jellyfish |                    | dd2f94a9-ab90-4e67-b608-9bfd7314cc41 |            0 |                11389    |
| Stylight               | 0012400000UUm1bAAD | fdbf87c7-1410-4b5a-a330-7b7ed8b22258 |            0 |                 8309    |
| Nickelodeon            | 0012400001A8rrsAAB | 879e50f7-9d71-4888-8f56-bec4b9fb6c6e |            0 |                 3049    |
| Zuspresso(M) SDN BHD   | 0011p00002bb9clAAA | d38a0981-6e82-40f4-8e72-2db2d48fbedb |            0 |                 3011.26 |
| Finlayson Oy           | 0010800002ptfRIAAY | 214d2291-f07f-45bc-b312-998cc5df41b9 |            0 |                 2700    |
| CFI Marketing          |                    | 9eeac3da-b806-4451-a2ec-ebc8c6cb6836 |            0 |                 2000    |
| hardtofind.com.au      | 0012400000OytmeAAB | b29b0717-c9d2-45ba-9f5b-588e622d2069 |            0 |                 1315.02 |
| Autodealers Digital    | 0010800003LDx1IAAT | a7a7ca1a-2b71-4086-ae87-6985d9e23bf5 |            0 |                 1099    |
| FlexShopper            | 0011p00002ebuz0AAA | e6420ee8-2a6b-4602-8bf9-81af36a59fa4 |            0 |                 1099    |
| Shades Media, Inc.     | 0010800003N4aPjAAJ | 291e41cb-8970-4045-87a8-6a7df78d5b09 |            0 |                 1099    |
