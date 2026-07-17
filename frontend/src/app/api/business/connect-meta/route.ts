import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const payload = await request.json();
    const backendUrl = process.env.MORLEN_BACKEND_URL || process.env.PYTHON_BACKEND_URL || 'http://127.0.0.1:8000';

    // 1. Post to OAuth meta endpoint (simulate or real)
    const oauthPayload = {
      business_id: payload.business_id,
      whatsapp_phone_id: process.env.WHATSAPP_PHONE_NUMBER_ID || payload.real_phone_id || "mock_demo_phone_id",
      meta_access_token: process.env.META_ACCESS_TOKEN || payload.real_access_token || "mock_demo_token"
    };

    let oauthRes;
    try {
      oauthRes = await fetch(`${backendUrl}/business/oauth/meta`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(oauthPayload)
      });
    } catch (fetchErr) {
      console.error('[API Connect Meta] Backend unreachable:', fetchErr);
      return NextResponse.json({ 
        error: 'Backend service is currently unavailable. Please try again later.',
        detail: 'Could not reach the Morlen backend server.' 
      }, { status: 503 });
    }

    if (!oauthRes.ok) {
      return NextResponse.json({ 
        error: `WhatsApp authentication failed (${oauthRes.status}).`,
        detail: 'Could not save OAuth tokens. Please verify your credentials.' 
      }, { status: 502 });
    }

    // 2. Post to Settings to save Owner Phone
    const phonePayload = {
      business_id: payload.business_id,
      owner_phone: payload.owner_phone
    };

    let phoneRes;
    try {
      phoneRes = await fetch(`${backendUrl}/business/settings/owner-phone`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(phonePayload)
      });
    } catch (fetchErr) {
      console.error('[API Connect Meta] Backend unreachable on phone save:', fetchErr);
      return NextResponse.json({ 
        error: 'Backend service is currently unavailable. Please try again later.',
        detail: 'Could not reach the Morlen backend server.' 
      }, { status: 503 });
    }

    if (!phoneRes.ok) {
      return NextResponse.json({ 
        error: `Failed to save your phone number (${phoneRes.status}).`,
        detail: 'Please try again.' 
      }, { status: 502 });
    }

    return NextResponse.json({ status: 'ok', message: 'WhatsApp connected successfully' });
  } catch (error) {
    console.error('[API Connect Meta] Unexpected error:', error);
    return NextResponse.json({ 
      error: 'Something went wrong. Please try again.',
      detail: 'An unexpected error occurred during WhatsApp connection.' 
    }, { status: 500 });
  }
}
