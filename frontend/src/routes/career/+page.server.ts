import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const careerUrl = 'http://backend:8000/api/career';

    const response = await fetch(careerUrl);

    if (!response.ok) {
        console.error(`Failed to Fetch Career ${response.status} ${response.statusText}`);
        return { profile: null };
    }

    const career = await response.json();

    return{
        career
    };
};