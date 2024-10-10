CREATE TABLE items (
    商品id VARCHAR(10) NOT NULL,
    商品名 VARCHAR(15) NOT NULL,
    カテゴリ VARCHAR(255) NOT NULL,
    価格 DECIMAL(10, 2) NOT NULL,
    在庫数 INT NOT NULL,
    説明 VARCHAR(100) NOT NULL,
    発売日 DATE NOT NULL,
    PRIMARY KEY (商品id)
);