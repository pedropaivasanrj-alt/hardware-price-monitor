CREATE TABLE IF NOT EXISTS stores (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    base_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    store_id INT NOT NULL REFERENCES stores(id),
    product_name TEXT NOT NULL,
    product_url TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    target_keyword TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS price_history (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(id),
    collected_at DATE NOT NULL,
    raw_price TEXT,
    price NUMERIC(10,2),
    availability TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(product_id, collected_at)
);
