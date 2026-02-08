import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
    const skillsUrl = 'http://backend:8000/api/skills';

    const response = await fetch(skillsUrl);

    if (!response.ok) {
        console.error(`Failed to Fetch Skills ${response.status} ${response.statusText}`);
        return { profile: null };
    }

    const skills = await response.json();

    return{
        skills
    };
};