import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const payload = await request.json();
    const pythonBackendUrl = process.env.PYTHON_BACKEND_URL || 'http://127.0.0.1:8000';

    // 1. Post to OAuth meta endpoint (simulate or real)
    const oauthPayload = {
      business_id: payload.business_id,
      whatsapp_phone_id: payload.real_phone_id || "mock_demo_phone_id",
      meta_access_token: payload.real_access_token || "mock_demo_token"
    };

    const oauthRes = await fetch(`${pythonBackendUrl}/business/oauth/meta`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(oauthPayload)
    });

    if (!oauthRes.ok) {
      throw new Error(`Failed to save OAuth tokens: ${oauthRes.statusText}`);
    }

    // 2. Post to Settings to save Owner Phone
    const phonePayload = {
      business_id: payload.business_id,
      owner_phone: payload.owner_phone
    };

    const phoneRes = await fetch(`${pythonBackendUrl}/business/settings/owner-phone`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(phonePayload)
    });

    if (!phoneRes.ok) {
      throw new Error(`Failed to save owner phone: ${phoneRes.statusText}`);
    }

    return NextResponse.json({ status: 'ok', message: 'WhatsApp connected successfully' });
  } catch (error) {
    console.error('[API Connect Meta] Error:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
