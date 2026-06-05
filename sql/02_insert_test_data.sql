-- Inserindo uma loja de teste
INSERT INTO stores (name, base_url)
VALUES ('Loja Teste', 'https://www.lojteste.com.br')
ON CONFLICT (name) DO NOTHING;

-- Inserindo um produto de teste
INSERT INTO products (
    store_id,
    product_name,
    product_url,
    category,
    target_keyword
)
VALUES (
    (SELECT id FROM stores WHERE name = 'Loja Teste'),
    'SSD Kingston NV2 500GB M.2 NVMe',
    'https://www.lojteste.com.br/ssd-kingston-nv2-500gb',
    'SSD M.2',
    'kingston nv2 500gb'
)
ON CONFLICT (product_url) DO NOTHING;

-- Inserindo preço com UPSERT
INSERT INTO price_history (
    product_id,
    collected_at,
    raw_price,
    price,
    availability
)
VALUES (
    (SELECT id FROM products WHERE product_url = 'https://www.lojteste.com.br/ssd-kingston-nv2-500gb'),
    CURRENT_DATE,
    'R$ 259,90',
    259.90,
    'Disponível'
)
ON CONFLICT (product_id, collected_at)
DO UPDATE SET
    raw_price = EXCLUDED.raw_price,
    price = EXCLUDED.price,
    availability = EXCLUDED.availability,
    created_at = NOW();