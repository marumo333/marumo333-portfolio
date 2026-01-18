FROM node:20-slim

WORKDIR /app

COPY package*.json ./
RUN npm install

# サーバーを外部（ホスト側）に公開するために --host オプションが必須
CMD ["npm", "run", "dev", "--", "--host"]