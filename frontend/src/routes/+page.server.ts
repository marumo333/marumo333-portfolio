import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
	const profileUrl = 'http://backend:8000/api/profile/me';

	const response = await fetch(profileUrl);

	if (!response.ok) {
		console.error(`Failed to Fetch Profile ${response.status} ${response.statusText}`);
		return { profile: null };
	}

    const profile = await response.json();

    return{
        profile
    };
};
