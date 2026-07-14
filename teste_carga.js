import http from 'k6/http';
export function setup() {
console.log("\n--- Teste de Carga executado por: [Johao, Rafael, Ysack] ---\n");
}
// Configuração do Desafio Bônus (Escalonamento de Carga)
export const options = {

stages: [
{ duration: '10s', target: 10 }, // Estágio 1: 10 usuários
{ duration: '10s', target: 100 }, // Estágio 2: 100 usuários
{ duration: '10s', target: 500 }, // Estágio 3: 500 usuários (Ponto de estresse)
],
};
// Função executada pelos usuários virtuais (VUs)
export default function () {
http.get('https://test.k6.io');
}