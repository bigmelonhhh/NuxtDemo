export function useApi<T>(path: string, options = {}) {
  const config = useRuntimeConfig()

  return useFetch<T>(path, {
    baseURL: config.public.apiBase || undefined,
    ...options,
  })
}
