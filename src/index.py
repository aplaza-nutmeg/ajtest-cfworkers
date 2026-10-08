from workers import WorkerEntryPoint, Response

class Default(WorkerEntryPoint):
    async def fetch(self, request):
        return Response("Hello AJ and Team from Python Worker!")