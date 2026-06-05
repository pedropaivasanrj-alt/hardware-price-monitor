from loaders.postgres_loader import (
    upsert_store,
    upsert_product,
    upsert_price_history
)


def main():
    print("Iniciando pipeline de teste...")

    store_id = upsert_store(
        name="Loja Teste Python",
        base_url="https://www.lojapythonteste.com.br"
    )

    print(f"Loja inserida/atualizada com ID: {store_id}")

    product_id = upsert_product(
        store_id=store_id,
        product_name="SSD Kingston NV2 500GB M.2 NVMe",
        product_url="https://www.lojapythonteste.com.br/ssd-kingston-nv2-500gb",
        category="SSD M.2",
        target_keyword="kingston nv2 500gb"
    )

    print(f"Produto inserido/atualizado com ID: {product_id}")

    upsert_price_history(
        product_id=product_id,
        raw_price="R$ 259,90",
        price=259.90,
        availability="Disponivel"
    )

    print("Historico de preco inserido/atualizado com sucesso.")
    print("Pipeline finalizado.")


if __name__ == "__main__":
    main()