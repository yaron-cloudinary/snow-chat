def get_mock_sql():
    return """WITH RankedAccounts AS (
    SELECT
        NAME,
        PLAN_SEGMENT,
        MRR_DOLLAR,
        ROW_NUMBER() OVER (PARTITION BY PLAN_SEGMENT ORDER BY MRR_DOLLAR DESC) AS rank
    FROM
        dim.accounts
    WHERE
        PAYING = TRUE
)

SELECT
    NAME,
    PLAN_SEGMENT,
    MRR_DOLLAR
FROM
    RankedAccounts
WHERE
    rank <= 5
ORDER BY
    PLAN_SEGMENT,
    MRR_DOLLAR DESC;"""