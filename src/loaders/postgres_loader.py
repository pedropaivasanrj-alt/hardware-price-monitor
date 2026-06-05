import psycopg2
from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def upsert_store(name: str, base_url: str) -> int:
    query = """
        INSERT INTO stores (name, base_url)
        VALUES (%s, %s)
        ON CONFLICT (name)
        DO UPDATE SET
            base_url = EXCLUDED.base_url
        RETURNING id;
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, base_url))
            store_id = cursor.fetchone()[0]
            return store_id


def upsert_product(
    store_id: int,
    product_name: str,
    product_url: str,
    category: str,
    target_keyword: str
) -> int:
    query = """
        INSERT INTO products (
            store_id,
            product_name,
            product_url,
            category,
            target_keyword
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (product_url)
        DO UPDATE SET
            product_name = EXCLUDED.product_name,
            category = EXCLUDED.category,
            target_keyword = EXCLUDED.target_keyword
        RETURNING id;
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                query,
                (
                    store_id,
                    product_name,
                    product_url,
                    category,
                    target_keyword
                )
            )
            product_id = cursor.fetchone()[0]
            return product_id


def upsert_price_history(
    product_id: int,
    raw_price: str,
    price: float,
    availability: str
) -> None:
    query = """
        INSERT INTO price_history (
            product_id,
            collected_at,
            raw_price,
            price,
            availability
        )
        VALUES (%s, CURRENT_DATE, %s, %s, %s)
        ON CONFLICT (product_id, collected_at)
        DO UPDATE SET
            raw_price = EXCLUDED.raw_price,
            price = EXCLUDED.price,
            availability = EXCLUDED.availability,
            created_at = NOW();
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                query,
                (
                    product_id,
                    raw_price,
                    price,
                    availability
                )
            )