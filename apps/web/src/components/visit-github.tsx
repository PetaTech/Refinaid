import { Button } from "@/components/ui/button"
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import { Github } from "lucide-react"


export function VisitGitHub() {
  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          <Button
            className="rounded-full w-8 h-8 bg-background mr-2"
            variant="outline"
            size="icon"
            onClick={() => window.open('https://github.com/1chooo/refinaid', '_blank')}
          >
            <Github />
          </Button>
        </TooltipTrigger>
        <TooltipContent>
          <p>Get Source Code</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  )
}
