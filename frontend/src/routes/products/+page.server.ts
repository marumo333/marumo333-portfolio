import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const productsUrl = 'http://backend:8000/api/products';

    const response = await fetch(productsUrl);

    if (!response.ok) {
        console.error(`Failed to Fetch Products ${response.status} ${response.statusText}`);
        return { profile: null };
    }

    const products = await response.json();

    return{
        products
    };
};