// Vercel serverless function: email capture for skills.aaxelera.com.
// Adds the lead to an Instantly list (and optional campaign) so nurture starts in the tool we already run.
// Env: INSTANTLY_API_KEY (required), INSTANTLY_LIST_ID (required), INSTANTLY_CAMPAIGN_ID (optional), NOTIFY_WEBHOOK (optional).
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'POST only' });
  const { email, name = '', market = '', source = 'skills.aaxelera.com' } = req.body || {};
  if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return res.status(400).json({ ok: false, error: 'valid email required' });
  const key = process.env.INSTANTLY_API_KEY, list = process.env.INSTANTLY_LIST_ID, campaign = process.env.INSTANTLY_CAMPAIGN_ID;
  if (!key || !list) return res.status(500).json({ ok: false, error: 'capture not configured' });
  const body = { email, first_name: name.split(' ')[0] || '', list_id: list, skip_if_in_workspace: true, custom_variables: { source, market: String(market).slice(0, 400), captured_at: new Date().toISOString() } };
  if (campaign) body.campaign = campaign;
  const r = await fetch('https://api.instantly.ai/api/v2/leads', { method: 'POST', headers: { 'Authorization': `Bearer ${key}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  if (!r.ok) return res.status(502).json({ ok: false, error: `instantly ${r.status}` });
  if (process.env.NOTIFY_WEBHOOK) { try { await fetch(process.env.NOTIFY_WEBHOOK, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text: `New map request: ${email} ${name}\nMarket: ${String(market).slice(0, 400) || '(none given)'}` }) }); } catch (e) {} }
  return res.status(200).json({ ok: true });
}
